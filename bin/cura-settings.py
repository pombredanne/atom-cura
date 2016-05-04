#!/usr/bin/env python3
import configparser, json

__doc__ = """
Extracts settings from the old ATOM2.0 CURA configuration and tries to match
them with newer CURA settings. This script is mainly used to inform the
writing of the `src/atom.yaml` file.
"""

# Loads the original Atom config
c = configparser.ConfigParser()
c.readfp(open("etc/ATOM2.0_CURA_settings_r1.ini"))
profile = c.items("profile")

def find_setting( setting, settings ):
	if setting in settings: return setting
	matching = [_ for _ in settings if _.find(setting) >= 0]
	return matching

# Loads the fdmprinter.json
def extract_settings(config,res=None):
	res = set() if res is None else res
	for k,v in config.items():
		if k in ("settings", "machine_settings"):
			for _ in v:
				res.add(_)
		elif isinstance(v,dict):
			extract_settings(v, res)
	return res
settings = extract_settings(json.load(open("etc/fdmprinter.json")))

# Now, for each profile value, we output if there is a corresponding override
not_found = []
for name, value in profile:
	#print (name, find_setting(name, settings))
	if name in settings:
		print ("{0}:\n\tdefault:{1}".format(name, value))
	elif name not in not_found:
		not_found.append(name)

for name in not_found:
	print ("[!] {0} : {1}".format(name, find_setting(name, settings) or "not found"))

#for name, value in c.items("profile"):
