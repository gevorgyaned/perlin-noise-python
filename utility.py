import vector
import math

def lerp(t):
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

