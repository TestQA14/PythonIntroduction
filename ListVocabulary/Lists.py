#!/usr/bin/env python
# -*- coding: utf-8 -*-

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
        ' Friday', 'Saturday', 'Sunday')

colors = ['blue', 'white', 'black', 'red', 'green', 'yellow']
print colors[0:3]

#add new color
colors.append('grey')
print colors

#delete black
del colors[2]
print colors
#or pop
colors.pop(2)
print colors

#vocabulary

book = {
    'User1 Test1': 3809326238,
    'User2 Test2': 3989090989,
    'User3 Test3': 3809384384,
}
#add new user
book['User4 Test4'] = 380949343
print book

#edit user info
book['User1 Test1'] = 0
print book

#del user
del book['User1 Test1']
print book

