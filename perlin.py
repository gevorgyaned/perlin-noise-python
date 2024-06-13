import math, random
from vector import Vector2
from utility import linear, lerp

GRID_SIZE = 256

class Perlin:
 def __init__(self):
  self.__perms = [i for i in range(GRID_SIZE)]
  random.shuffle(self.__perms)
  
  for i in range(GRID_SIZE):
   self.__perms.append(self.__perms[i])
  
  self.__grads = []
  for i in range(GRID_SIZE):
    val = random.random() * math.pi * 2
    self.__grads.append(Vector2(math.sin(val), math.cos(val)))
  
 def __get_gradient(self, x, y):
  return self.__grads[self.__perms[self.__perms[x % GRID_SIZE] + y % GRID_SIZE] % GRID_SIZE]

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

  u = lerp(dx)
  v = lerp(dy)

  li1 = linear(u, dot_tl, dot_tr)
  li2 = linear(u, dot_bl, dot_br)

  return linear(v, li1, li2)
