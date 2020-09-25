.PHONY: build generate clean

build:
	python build/builder.py n

build-all:
	python build/builder.py y

generate:
	rm -rf k8sgen/data
	cp -r data k8sgen/data
	python build/generator.py

docs:
	cd k8sgen/docs; make html