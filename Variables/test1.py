#!/usr/bin/env python
# -*- coding: utf-8 -*-


print "Variables Demo"

v = 1
print "v = ", v

v = v + 2
print "v + 2 = ", v

v = 52
print "v = ", v

print "v * 5 = ", v*5

print "v = ", v

v = v * 5
print "v = v * 5"
print "v = ", v

word1 = "Good"

word2 = "Morning"
word3 = "to you too!"

print word1, word2
sentence = word1 + " " + word2 + " " + word3
print sentence


i =0
while i < 10:
    i = i + 1
    print i

i =10
while i != 0:
    print i
    i = i -1
    print "i = ", i
print "End of 'while' cycle"

x = 1
if x == 1:
    print 'x = ', x

i = 1
while i <= 20:
    if i % 2 == 0:
        print i
    i = i + 1
print 'done....'

k = 1
if k > 5:
    print 'no chances!'
else:
    print 'to be printed'

a = 4
if a > 50:
    print 'this is wrong!'
elif a < 8:
    print 'this is right!'

a = raw_input("What is your name?")
print a