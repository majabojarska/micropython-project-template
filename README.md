# micropython-project-template

A [MicroPython](https://micropython.org/) project template.

> [!WARNING]
> This is an early work in progress. Use this template at your own risk.

![Status](https://github.com/majabojarska/micropython-project-template/actions/workflows/status.yaml/badge.svg) [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

## Planned work

- [x] Add example, non-flatPython project sources.
- [x] Setup a build toolchain.
- [x] Implement build, upload, lint, and format targets.
- [ ] Add license.
- [x] Add code of conduct.
- [ ] Setup project template generation workflows.
- [ ] Add issue templates.
- [ ] Add contribution guidelines.

## Development

### Setup environment

```bash
# Create a virtualenv, or use your preferred approach instead.
virtualenv .venv --python=python3.10

# Activate
source .venv/bin/activate

# Install project in editable mode with dev and test dependency extras
pip install -e '.[dev,test]'

# Setup pre-commit
pre-commit install
```

### Build, deploy

```bash
# Use this for a quick development feedback loop.
make run-remote

# Use this for persistent board flashing.
make build
make upload
```

See the [Makefile](./Makefile) for more details on the above targets, and more.

## Attributions

- [Linting with Ruff and cross-compiling bytecode](https://github.com/orgs/micropython/discussions/13152)
- [rshell - Remote Shell for MicroPython ](https://github.com/dhylands/rshell)
- [Install micropython GitHub Action](https://github.com/marketplace/actions/install-micropython)
- [Micropython Stubs](https://github.com/Josverl/micropython-stubs)
- [Using Pytest with MicroPython - HW in the loop](https://resources.altium.com/p/automating-micropython-development-and-testing-using-continuous-integration)
- [Setting up a language server to use micropython stubs](https://micropython-stubs.readthedocs.io/en/main/22_vscode.html)
