.PHONY: build generate clean build-all docs bump-major bump-minor bump-patch pypi-build pypi-test pypi-upload

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

pypi-build:
	python setup.py sdist bdist_wheel
	twine check dist/*

pypi-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi-upload:
	twine upload dist/*