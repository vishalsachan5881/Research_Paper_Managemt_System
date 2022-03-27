from operator import truediv
from re import S
import re
from select import select
from tkinter import N
from tkinter.tix import ButtonBox
import copy
import random


print(random.randint(0, 1))
print(random.randint(0, 1))
print(random.randint(0, 1))
print(random.randint(0, 1))
print(random.randint(0, 1))


class Rec:
    def __init__(self, l, w, x, y):
        self.l = l
        self.w = w
        self.corner = Point(x, y)

    def center(self):
        return Point(
            self.corner.x + self.w/2,
            self.corner.y + self.l/2,

        )


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self) -> None:
        print(
            f"x cordinate = {self.x} and y cordinate = {self.y} {self.drew()}")

    # def __str__(self):
    #     return f"point({self.x},{self.y})"

    def drew(self):
        print(4)


def add_Point(p, q):
    return Point((p.x+q.x), p.y + q.y)


def summ(a, b):
    print(a, b)
    return a+b


egg = 100


def spam():
    print(egg)


spam()


# point = Point(1, 2)
# point1 = Point(1, 2)
# ans = add_Point(point1, point)
# print(ans.x, ans.y)
# box = Rec(100, 200, 1, 3)
# print("hiiiiiiiiiiiiiiiii")
# print(box.corner.x, "hiiiiiii ")

# p = box.center()
# print(p.x, p.y)

# q = p
# q = copy.deepcopy(p)
# q.x = 22
# print(p == q)

# print(q.x, q.y)
# print(p.x, p.y)


# box1 = copy.deep
# copy(box)
# print(box1 == box)
# print(box1.corner == box.corner)
# # print("jaaa")
# # print(type(point))
# # print(isinstance(point, Point))
# # # point.draw()
# # print(point.x, point.y)
# print(point.draw())
# print(f"point({point.x} , {point.y})")
# print(str(point))
# print(point)
# print(str(point))


d = summ(b=3, a=2)
print(d)


l = [1, 2, 3]
l.sort(reverse=True)
print(l)
