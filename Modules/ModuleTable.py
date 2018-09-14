#!/usr/bin/env python
# -*- coding: utf-8 -*-


years = 8
apples = 23


def hello_world():
    print "Hi there"


def multiply(value):
    print value * 4


class Table:

    def __init__(self):
        self.color = raw_input(u"Какой цвет стола? ")
        self.height = raw_input(u"Какая высота стола? ")
        self.price = raw_input(u"Какая цена стола? ")

    def details(self):
        print u"Этот стол имеет высоту " + self.height + u" метров"
        print u"Этот стол стоит " + self.price + u" гривен"

