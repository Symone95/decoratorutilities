#from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decoratorutilities",
    version="1.0",
    author="Giovanni Cardamone, Scalamandrè Simone",
    author_email="giovanni.cardamone@sourcesense.com, simone.scalamandre@sourcesense.com",
    description="Python library to user type guard utilities to check parameters and return type, allow function overloading and function mocking at runtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
