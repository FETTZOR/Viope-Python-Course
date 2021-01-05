# -*- coding: cp1252 -*-

number = int(input("Give a number: "))
i = 0
y = 0
result = 0
for i in range(0, number, 1):
    result = i + result
    print("The sum was:", result)

