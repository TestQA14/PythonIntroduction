#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    description = "Этот прямоугольник не имеет пока описание"
    author = "Этот прямоугольник не имеет автора пока"

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def author_name(self, text):
        self.author = text

    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale


my_rect = Rectangle(60, 25)
print my_rect.area()
print my_rect.perimeter()
my_rect.describe("This is a new rectangle")
my_rect.author_name("Tester")
my_rect.scaleSize(0.5)
print my_rect.area()
print my_rect.description
print my_rect.author


long_rect = Rectangle(120, 10)
short_rect = Rectangle(30, 10)


