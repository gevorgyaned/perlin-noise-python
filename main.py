from perlin import Perlin
from vector import Vector2
from PIL import Image
from utility import fbm

IM_WIDTH = 360
IM_HEIGHT = 360 

SCALE = 40 

noise = Perlin()
image = Image.new("RGB", (IM_WIDTH, IM_HEIGHT))

pixels = image.load()

for i in range(IM_WIDTH):
 for j in range(IM_HEIGHT):
  val = fbm(noise, i / SCALE, j / SCALE) 
  normal_val = val * 255
  pixels[i, j] = (int(normal_val), int(normal_val), int(normal_val))

image.show()
