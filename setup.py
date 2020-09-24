import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decoratorutilities",
    version="1.0.1",
    author="Scalamandrè Simone, Giovanni Cardamone",
    author_email="simone.scalamandre@sourcesense.com, giovanni.cardamone@sourcesense.com",
    description="Python library to user type guard utilities to check parameters and return type, allow function overloading and function mocking at runtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Symone95/decoratorutilities",
    packages=["decoratorutilities"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',

)
