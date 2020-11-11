.PHONY: build generate clean build-all docs bump-major bump-minor bump-patch pypi

build:
	python build/builder.py n

build-all:
	python build/builder.py y

generate:
	python build/generator.py

docs:
	cd k8sgen/docs; make html

bump-major:
	bumpversion major src/aphelper/VERSION

bump-minor:
	bumpversion minor src/aphelper/VERSION

bump-patch:
	bumpversion patch src/aphelper/VERSION

pypi:
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	twine upload dist/*