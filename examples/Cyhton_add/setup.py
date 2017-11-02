from distutils.core import setup,Extension
from Cython.Build import cythonize

ext = Extension(
    "addfunc",
    sources=["use_add.pyx", "addfunc.cpp"],
    language="c++"
)

setup(
    ext_modules=cythonize(ext)
)