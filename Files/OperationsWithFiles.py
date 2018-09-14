#!/usr/bin/env python
# -*- coding: utf-8 -*-


# open file for reading
myFile = open ('/Users/irinachemisova/Desktop/TestText.txt', 'r')

print myFile.read()

# To return pointer to begining of file
myFile.seek(0)

# To find out current position of pointer
myFile.tell()

# To read file from current position of pointer to end of row
myFile.readline()

# To read file from current position of pointer to end of file
myFile.readlines()

# open file for writing
myFile = open ('/Users/irinachemisova/Desktop/TestText.txt', 'w')

myFile.write('Hello World')

myFile.close()
