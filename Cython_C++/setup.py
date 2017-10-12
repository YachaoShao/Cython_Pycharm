# from distutils.core import setup, Extension
# from Cython.Build import cythonize
#
# setup(ext_modules=cythonize(Extension(
#            "rect",                 # the extension name
#            sources=["rect.pyx", "Rectangle.cpp"],  # additional source file(s)
#            language="c++",             # generate C++ code
#       )))

from distutils.core import setup,Extension
from Cython.Build import cythonize

ext = Extension(
        "rect",
        sources=['rect.pyx', 'Rectangle.cpp'],
        language='c++'
        )

setup(ext_modules=cythonize(ext))




