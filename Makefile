.PHONY: pipsetup build clean full_clean

PYTHON_VERSION = 3.14

.venv/bin/activate:
	python${PYTHON_VERSION} -m venv .venv

build:
	.venv/bin/pip install --upgrade build
	.venv/bin/python -m build

clean:
	rm -rf dist

full_clean:
	rm -rf dist
	rm -rf site
