import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decoratorutilities",
    version="1.0.2",
    author="Scalamandrè Simone, Giovanni Cardamone",
    author_email="simone.scalamandre@sourcesense.com, giovanni.cardamone@sourcesense.com",
    description="DecoratorUtilities is a python library that provides different utilities for functions and class methods such as to check parameters and return type, allow overloading, to cache results to speed up them, instantiate a Singleton object and mocking at runtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Symone95/decoratorutilities",
    download_url="https://pypi.org/project/decoratorutilities/#files",
    packages=["decoratorutilities"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',

)
