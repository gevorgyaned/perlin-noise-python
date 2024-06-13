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

colors = [
	(0, 0, 128),
	(0, 0, 255), 
	(144, 238, 144),
	(34, 139, 34),
	(0, 100, 0),
	(85, 107, 47),  
	(107, 142, 35), 
	(160, 82, 45),  
	(139, 69, 19),
	(101, 67, 33),
	(169, 169, 169),
	(105, 105, 105),
	(255, 255, 255),
	(224, 255, 255) 
]

for i in range(IM_WIDTH):
  for j in range(IM_HEIGHT):  
    val = fbm(noise, i / SCALE, j / SCALE)
    val = (val / 2 + 0.5)
    pixels[i, j] = colors[int(val * len(colors))]

image.show()
