import perlin
from vector import Vector2
from PIL import Image
from utility import fbm

noise = perlin.Perlin()
image = Image.new("RGB", (perlin.IM_WIDTH, perlin.IM_HEIGHT))

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

for i in range(perlin.IM_WIDTH):
  for j in range(perlin.IM_HEIGHT):  
    val = fbm(noise, i / perlin.SCALE, j / perlin.SCALE)
    val = (val / 2 + 0.5)
    pixels[i, j] = colors[int(val * len(colors))]

image.show()
