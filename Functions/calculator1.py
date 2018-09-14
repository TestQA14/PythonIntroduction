#!/usr/bin/env python
# -*- coding: utf-8 -*-


loop = 1

choice = 0


def menu():
    print "We have several operations : "
    print "Option 1 - plus"
    print "Option 2 - minus"
    print "Option 3 - multiply"
    print "Option 4 - divide"
    print "Option 5 - exit"
    return input("Please, select operation: ")


def add(num1, num2):
    print num1, " + ", num2, " = ", num1 + num2


def minus(num1, num2):
    print num1, " - ", num2, " = ", num1 - num2


def multiply(num1, num2):
    print num1, " * ", num2, " = ", num1 * num2


def divide(num1, num2):
    print num1, " / ", num2, " = ", num1 / num2


while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("The first number: "), input("The second number: "))
    elif choice ==  2:
        minus(input("The first number: "), input("The second number: "))
    elif choice == 3:
        multiply(input("The first number: "), input("The second number: "))
    elif choice == 4:
        divide(input("The first number: "), input("The second number: "))
    elif choice == 5:
        loop == 0
print "See you soon! "
