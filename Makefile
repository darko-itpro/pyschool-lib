.PHONY: clean build

PYTHON_VERSION = 3.13

.venv/bin/activate: requirements.txt
	python${PYTHON_VERSION} -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install --upgrade -r requirements.txt

build:
	.venv/bin/pip install --upgrade build
	.venv/bin/python -m build

clean:
	rm -rf dist

full_clean:
	rm -rf dist
	rm -rf .venv
