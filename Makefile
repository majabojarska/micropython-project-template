DIR_SOURCES ?= src
DIR_BUILD ?= build

# RP2040: armv6m
ARCH ?= armv6m 

DEVICE ?= /dev/ttyACM0
DIR_RSHELL_FLASH ?= /pyboard

all: lint test build

.PHONY: build
build: fmt lint test clean
	python3 scripts/build.py --src $(DIR_SOURCES) --dest $(DIR_BUILD) --arch $(ARCH)

.PHONY: clean
clean:
	rm -rf build/*

.PHONY: upload
upload: 
	$(MAKE) clean
	echo "Removing existing build artifactos on remote"
	rshell rsync --mirror $(DIR_BUILD) $(DIR_RSHELL_FLASH)
	
	$(MAKE) build
	rshell rsync --mirror $(DIR_BUILD) $(DIR_RSHELL_FLASH)
	$(MAKE) reset

# Mount local sources on remote and run the project.
.PHONY: run-remote
run-remote: build
	mpremote mount $(DIR_SOURCES) exec "import boot; import main"

.PHONY: reset
reset:
	mpremote reset

.PHONY: repl
repl:
	rshell repl --port $(DEVICE)

.PHONY: test
test:
	pytest

.PHONY: lint
lint:
	ruff check
	ruff format --check

.PHONY: fmt
fmt:
	ruff format
