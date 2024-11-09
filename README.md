# micropython-project-template

A MicroPython project template.

![Status](https://github.com/majabojarska/micropython-project-template/actions/workflows/status.yaml/badge.svg)

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
