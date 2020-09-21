#from distutils.core import setup
import setuptools

#packages=['typeguard',],
#license='Creative Commons Attribution-Noncommercial-Share Alike license',
#long_description=open('README.md').read(),

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TypeGuard", # Replace with your own username
    version="1.0",
    author="Giovanni Cardamone, Scalamandrè Simone",
    author_email="giovanni.cardamone@sourcesense.com, simone.scalamandre@sourcesense.com",
    description="A small example package",
    long_description= long_description,
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