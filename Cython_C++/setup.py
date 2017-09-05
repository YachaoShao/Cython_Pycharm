from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules=cythonize(Extension(
           "rect.pyx",                 # our Cython source
           sources=["Triangle.cpp"],  # additional source file(s)
           language="c++",             # generate C++ code
      )))
