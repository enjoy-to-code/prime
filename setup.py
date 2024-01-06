# setup.py
from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize(
        "primes_cython.pyx", annotate=True
    ),
)
