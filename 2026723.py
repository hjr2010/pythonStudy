from datetime import date

d1 = date(2016, 7, 1)
print(str(d1))
d2 = date(2026, 7, 23)
print(str(d2))
delta = d2 - d1
print(delta.days)
import math

class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Square):
    def __init__(self, width, height):
        super().__init__(width)
        self.height = height

    def get_area(self):
        return self.side * self.height

class Circular(Square):
    def get_area(self):
        return math.pi * self.side ** 2

class Triangle(Square):
    def get_area(self):
        return (math.sqrt(3) / 4) * self.side ** 2


shape_type = input().strip()
nums = list(map(int, input().split()))

area = 0
class_name = shape_type
cls = globals()[class_name]
obj = cls(nums[0])
area = obj.get_area()
print(area)
'''
if shape_type == "Square":
    obj = Square(nums[0])
    area = obj.get_area()
    print(int(area))
elif shape_type == "Rectangle":
    obj = Rectangle(nums[0], nums[1])
    area = obj.get_area()
    print(int(area))
elif shape_type == "Circular":
    obj = Circular(nums[0])
    area = obj.get_area()
    print("{0:.3f}".format(area))
elif shape_type == "Triangle":
    obj = Triangle(nums[0])
    area = obj.get_area()
    print("{0:.3f}".format(area))
    '''
a = [5, 9, 3, 7, 2, 6]
# 选择排序
for i in range(len(a)-1):
    start_index = i   
    for j in range(i + 1, len(a)):
        if a[start_index] > a[j]:
            start_index = j
    print(a[start_index])
    a[i], a[start_index] = a[start_index], a[i]
    print(a)
