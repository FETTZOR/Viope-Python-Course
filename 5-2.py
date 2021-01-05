# -*- coding: cp1252 -*-

filename = input("Give a file name: ")

file = open(filename, 'w')

text_for_file = input("Write something: ")
file.write(text_for_file)

print("Wrote ", text_for_file, " to the file ", filename)
file.close()