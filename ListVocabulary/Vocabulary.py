#!/usr/bin/env python
# -*- coding: utf-8 -*-


planets = {}

planets['Earth'] = 12756
planets['Moon'] = 3476
planets['Mercury'] = 4880
planets['Jupiter'] = 142740

if planets.has_key('Earth'):
    print "Earth is a part of our solar system"
else:
    print "Earth doesn't exist"

print 'Our planets:'
print planets.keys()

keys = planets.keys()

print "Radiuses of panets are different:  ", planets.values()

values = planets.values()

print keys
keys.sort()
print keys

print values
values.sort()
print values

print "Quantity of planets: ", len(planets)