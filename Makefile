CURA         :=`which cura`
CURA_PREFIX  :=`which cura|xargs dirname|xargs dirname`
STL_PATH      =$(CURA_PREFIX)/share/cura/resources/meshes/atom.stl
JSON_PATH     =$(HOME)/.local/share/cura/machines/atom.json

.PHONY: install yaml2json cura

install: dist/atom.json dist/atom.stl cura 
	@echo "[>] Copying Atom bed mesh to $(STL_PATH)"
	@sudo cp dist/atom.stl $(STL_PATH)
	@echo "[>] Copying Atom machine configuration to $(JSON_PATH)"
	@cp   dist/atom.json $(JSON_PATH)
	@echo "[ ] All done!"

yaml2json:
	@echo "[ ] Looking for $@"
	@which yaml2json > /dev/null

cura:
	@echo "[ ] Looking for $@"
	@which cura > /dev/null

dist/%.json: src/%.yaml yaml2json
	@echo "[<] Compiling $< to $@"
	@yaml2json $< > $@

# EOF
