#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "Hello!"

loop = 1

choice = 0

while loop == 1:
    print "We have several operations : "
    print "Option 1 - plus"
    print "Option 2 - minus"
    print "Option 3 - multiply"
    print "Option 4 - divide"
    print "Option 5 - exit"

    choice = input("Please, select operation ")
    if choice == 1:
        print "You chosen +"
        num1 = input("Please input the first number ")
        num2 = input("Please input the second number ")
        print num1, " + ", num2, " = ", num1 + num2
    if choice == 2:
        print "You chosen -"
        num1 = input("Please input the first number ")
        num2 = input("Please input the second number ")
        print num1, " - ", num2, " = ", num1 - num2
    if choice == 3:
        print "You chosen *"
        num1 = input("Please input the first number ")
        num2 = input("Please input the second number ")
        print num1, " * ", num2, " = ", num1 * num2
    if choice == 4:
        print "You chosen /"
        num1 = input("Please input the first number ")
        num2 = input("Please input the second number ")
        print num1, " / ", num2, " = ", num1 / num2
    if choice == 5:
        loop == 0
print "See you soon!"

