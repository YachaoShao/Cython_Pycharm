from distutils.core import setup
from Cython.Build import cythonize

setup(
    ex_modules = cythonize("fibnacci.pyx")
)