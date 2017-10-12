#!/usr/bin/env python
# coding=utf-8

import rect

#if __name__ == "__main__":
pyRect = rect.PyRectangle(1,2,3,4)
width, height = pyRect.get_size()
point_x, point_y = pyRect.getPoint()
print("size:width = %d, height = %d" % (width, height))
print("the area of the rectangle is %d" % pyRect.get_area())
print("the first point of the rectangle is (%d,%d)" % (point_x, point_y))










