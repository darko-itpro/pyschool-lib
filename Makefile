setup:
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	pip install --upgrade build

build: setup
	python -m build

clean:
	rm -rf dist
