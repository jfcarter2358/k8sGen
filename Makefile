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
	bumpversion major k8sgen/VERSION

bump-minor:
	bumpversion minor k8sgen/VERSION

bump-patch:
	bumpversion patch k8sgen/VERSION

pypi:
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	twine upload dist/*