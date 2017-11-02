from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    # module information
    # name="edlib"
    # version="1.0"
    # url="https://github.com/YachaoShao/Cython_Pycharm"
    # author="Yachao Shao"
    # license="JSC"
    # keywords="Test setuptools module"

    # Build instructions
    ext_modules=cythonize("cythonhello.pyx"))
