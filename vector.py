class Vector2:
 def __init__(self, a, b):
  self.a = a
  self.b = b

 def dot(self, other):
  return self.a * other.a + self.b * other.b
