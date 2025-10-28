.PHONY: pipsetup build clean full_clean

PYTHON_VERSION = 3.13

.venv/bin/activate:
	python${PYTHON_VERSION} -m venv .venv

pipsetup: requirements.txt
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install --upgrade -r requirements.txt

build:
	.venv/bin/pip install --upgrade build
	.venv/bin/python -m build

clean:
	rm -rf dist

full_clean:
	rm -rf dist
	rm -rf site
