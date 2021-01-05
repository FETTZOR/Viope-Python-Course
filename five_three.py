# -*- coding: cp1252 -*-

filename = "strings.txt"
open_file = open("strings.txt", "r")
text = open_file.readlines()
for i in text:
    if i.rstrip().isalnum():
        print(i.rstrip(), " was ok.")
    else:
        print(i.rstrip(), " was invalid.")
open_file.close()