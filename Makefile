CURA=$(shell which cura)
CURA_PREFIX:=$(shell dirname $(CURA))
CURA_PREFIX:=$(shell dirname $(CURA_PREFIX))
STL_PATH=$(CURA_PREFIX)/share/cura/resources/meshes/atom.stl
JSON_PATH=$(HOME)/.local/share/cura/machines/atom.json

.PHONY: install yaml2json cura

yaml2json:
	which yaml2json

cura:
	which cura

install: yaml2json cura atom.stl atom.json
	@echo Copying Atom bed mesh to $(STL_PATH)
	@sudo cp atom.stl      $(STL_PATH)
	@echo Copying Atom machine configuration to $(JSON_PATH)
	@yaml2json atom.yaml > $(JSON_PATH)

%.json: %.yaml yaml2json
	yaml2json %< > $@

# EOF
