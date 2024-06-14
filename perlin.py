import math, random
from vector import Vector2
import utility

IM_WIDTH = 360
IM_HEIGHT = 360 

SCALE = 40 
GRID_SIZE = 256

class Perlin:
  def __init__(self):
    self.__grads = []
    for i in range(GRID_SIZE):
      tmp = []
      for j in range(GRID_SIZE):
        rnd = random.random() * math.pi * 2
        tmp.append(Vector2(math.sin(rnd), math.cos(rnd)))
      self.__grads.append(tmp)

  def __get_gradient(self, x, y):
    return self.__grads[x % GRID_SIZE][y % GRID_SIZE]

  def get_value(self, x, y):
    ix, iy = math.floor(x), math.floor(y)
    dx, dy = x - ix, y - iy
 
    tl = self.__get_gradient(ix, iy)
    tr = self.__get_gradient(ix + 1, iy)
    bl = self.__get_gradient(ix, iy + 1)
    br = self.__get_gradient(ix + 1, iy + 1)
 
    dot_tl = tl.dot(Vector2(dx, dy)) 
    dot_tr = tr.dot(Vector2(dx - 1, dy)) 
    dot_bl = bl.dot(Vector2(dx, dy - 1)) 
    dot_br = br.dot(Vector2(dx - 1, dy - 1)) 
 
    u = utility.fade(dx)
    v = utility.fade(dy)
 
    li1 = utility.linear(u, dot_tl, dot_tr)
    li2 = utility.linear(u, dot_bl, dot_br)
 
    return utility.linear(v, li1, li2)
 
