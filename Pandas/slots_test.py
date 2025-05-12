class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)

try:
  p.z = 3
except AttributeError as e:
    print(f"AttributeError: {e}")   

print(f"Point: x= {p.x}, y={p.y}")

import sys
class PointNoSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = PointNoSlots(10,20)

print(f"Size with slots: {sys.getsizeof(p)}")
print(f"Size without slots: {sys.getsizeof(p2)}")
