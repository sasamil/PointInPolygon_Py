# the representation of a point will be a tuple (x,y)
# the representation of a polygon wil be a list of points [(x1,y1), (x2,y2), (x3,y3), ... ]

# it is assumed that polygon is regular i.e. lines don't intersect each other (otherwise, it is questionable whether it is a polygon)

import sys
import copy
import time
import random

from pointInside import *

#-------------------------------------------------------------------------------
test_polygon2 = [ (0,1), (1,1), (1,2), (2,2), (2,3), (3,3), (3,2), (4,0), (5,9), (6,0), 
              (7,2), (8,0), (8,-2), (7,-3), (6,-2), (5,-2), (4,-2), (3,-1), (2,-2), (1,-2), 
              (0,-3), (-2,-3), (-3,-4), (-4,-3), (-5,-3), (-5,-2), (-4,-2), (-4,.5), (-5,.5), (-5,1), 
              (-4,1), (-4,2), (-4,4), (-3,4), (-3,2), (-2,2), (-2,0), (-1,1), (0,1) ]



#-------------------------------------------------------------------------------
def main():
  
  random.seed(1389)
  i = 0
  t = time.perf_counter()
  while i < 50000:
    testpoint = (0.1*random.randrange(-50, 80), 0.1*random.randrange(-40, 40))
    cn_PnPoly(testpoint, test_polygon2)
    i += 1
  
  print("cn_PnPoly() - execution time: " + str(time.perf_counter() - t))

  random.seed(1389)
  i = 0
  t = time.perf_counter()
  while i < 50000:
    testpoint = (0.1*random.randrange(-50, 80), 0.1*random.randrange(-40, 40))
    wn_PnPoly(testpoint, test_polygon2)
    i += 1
  
  print("wn_PnPoly() - execution time: " + str(time.perf_counter() - t))

  random.seed(1389)
  i = 0
  t = time.perf_counter()
  while i < 50000:
    testpoint = (0.1*random.randrange(-50, 80), 0.1*random.randrange(-40, 40))
    is_inside_postgis(test_polygon2, testpoint)
    i += 1
  
  print("is_inside_postgis() - execution time: " + str(time.perf_counter() - t))

  random.seed(1389)
  i = 0
  t = time.perf_counter()
  while i < 50000:
    testpoint = (0.1*random.randrange(-50, 80), 0.1*random.randrange(-40, 40))
    isPointInPath(testpoint, test_polygon2)
    i += 1
  
  print( "isPointInPath() - execution time: " + str(time.perf_counter() - t))

  random.seed(1389)
  i = 0
  t = time.perf_counter()
  while i < 50000:
    testpoint = (0.1*random.randrange(-50, 80), 0.1*random.randrange(-40, 40))
    is_inside_sm(test_polygon2, testpoint)
    i += 1
  
  print("is_inside_sm() - execution time: " + str(time.perf_counter() - t))

  

# -------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
