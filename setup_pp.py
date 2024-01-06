# compile.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "primes_pure_python.py", , annotate=True
    ),
)

