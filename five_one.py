# -*- coding: cp1252 -*-


handle = open("facts.txt", "r")
filetext = handle.read()
print("Following was read from the file: ", filetext)
handle.close()