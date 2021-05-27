dist: setup.py
	pip install -e .
	py -m build

check: dist
	py -m twine check dist/*

upload: dist
	py -m twine upload dist/*

all: dist

clean:
	rm -rf dist build

test:
	py -m unittest
