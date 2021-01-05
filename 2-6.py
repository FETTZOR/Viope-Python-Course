word = "desserts"
first_part = word[0:4]
second_part = word[-4:]


result = second_part[::-1] + first_part[::-1]
# rap = word[::-1]
print("The first 4 characters were: ", first_part)
print("The last 4 characters were: ", second_part)
print("The string backwards was:", result)
# print(rap)