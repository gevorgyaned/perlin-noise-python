from vector import Vector2
import math

def fade(t):
  return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

def linear(t, a, b):
  return a + t * (b - a)

def fbm(noise, x, y):
  value = 0
  frequency = 0.3
  amplitude = 1

  for i in range(6):
    value += noise.get_value(x * frequency, y * frequency) * amplitude
    amplitude *= 0.5
    frequency *= 2

  return value

def pseudo_rand(vec):
  x = math.sin(vec.dot(Vector2(12.9898, 78.233)) * 43758.5453)
  return Vector2(math.sin(x), math.cos(x))
