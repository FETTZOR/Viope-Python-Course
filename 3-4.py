first_number = int(input("Give a number: "))
second_number = int(input("Give another number: "))
if (first_number % 2 == 0) and (second_number % 2 == 0):
    print("Both numbers are even.")
elif(first_number % 2 == 0) or (second_number % 2 == 0):
    print("One of the numbers is even.")
else:
    print("Both numbers are odd.")
