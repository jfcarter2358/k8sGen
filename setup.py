import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="k8sgen",
    version="0.0.1",
    author="John Carter",
    author_email="jfcarter2358@gmail.com",
    description="A Python package to enable dynamic generation of Kubernetes manifests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfcarter2358/k8sGen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'k8sgen': ['data/APIResources/*.json', 'data/Components/*.json']},
    python_requires='>=3.7',
)