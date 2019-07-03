from setuptools import setup, find_packages

setup(
    name="PyCMeKG",
    version="0.2.2",
    author="Yunfei Yang",
    author_email="yfy@pku.edu.cn",
    description="Chinese Medical Knowledge Graph",
    long_description="Chinese Medical Knowledge Graph",
    license="MIT",
    url="https://github.com/king-yyf/PyCMeKG",
    packages=find_packages(),
    package_data={
        # If any package contains *.txt files, include them:
        '': ['*.txt'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        'pyCMeKG': ['data/*.pkl'],
    },

    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)