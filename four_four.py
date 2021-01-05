print("Calculator")
while True:
    first_number = int(input("Give the first number: "))
    second_number = int(input("Give the second number: "))
    print("(1) + \n(2) - \n(3) * \n(4) / \n(5) Change numbers \n(6) Quit\nCurrent numbers: ", first_number, " ", second_number + "\nPlease select something (1-6): ")
    operator = int(input( ))
    # ))
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
    elif operator == 5:
        first_number = int(input("Give the first number: "))
        second_number = int(input("Give the second number: "))
    elif operator == 6:
        print("Thank you!")
        break
    else:
        print("Selection was not correct.")