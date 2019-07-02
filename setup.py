from setuptools import setup, find_packages

setup(
    name="PyCMeKG",
    version="0.1.9",
    author="Yunfei Yang",
    author_email="yfy@pku.edu.cn",
    description="Chinese Medical Knowledge Graph",
    long_description="Chinese Medical Knowledge Graph",
    license="MIT",
    url="https://github.com/king-yyf/PyCMeKG",
    packages=find_packages(),

    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)