cdef extern from "Rectangle.h" namespace "shapes":
    cdef cppclass Rectangle:
        Rectangle() except +
        Rectangle(int, int, int, int) except +
        int x0, y0,
        int getArea()
        void getSize(int* width, int* height)
        void getPoint(int* point_x, int* point_y)
        void move(int, int)


cdef class PyRectangle:
    cdef Rectangle c_rect      # hold a C++ instance which we're wrapping
    def __cinit__(self, int x0, int y0, int x1, int y1):
        self.c_rect = Rectangle(x0, y0, x1, y1)
    def get_area(self):
        return self.c_rect.getArea()
    def get_size(self):
        cdef int width, height
        self.c_rect.getSize(&width, &height)
        return width, height
    def get_point(self):
        cdef int point_x, point_y
        self.c_rect.getPoint(&point_x, &point_y)
        return point_x, point_y
    def move(self, dx, dy):
        self.c_rect.move(dx, dy)
