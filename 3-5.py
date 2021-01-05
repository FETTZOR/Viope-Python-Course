print("Calculator")
first_number = int(input("Give the first number: "))
second_number = int(input("Give the second number: "))
operator = int(input("(1) + \n(2) - \n(3) * \n(4) / \nPlease select something (1-4): "))
if operator == 1:
    resultOfPlus = first_number + second_number
    print("The result is: ", resultOfPlus)
elif operator == 2:
    resultOfMinus = first_number - second_number
    print("The result is: ", resultOfMinus)
elif operator == 3:
    resultOfMultiplication = first_number * second_number
    print("The result is: ", resultOfMultiplication)
elif operator == 4:
    resultOfDivision = first_number / second_number
    print("The result is: ", resultOfDivision)
else:
    print("Selection was not correct.")