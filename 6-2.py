def poweroftwo(number):
    result = 1
    number_two = 2
    for i in range(0, number, 1):
        result = number_two * result
    print("The result is ", result)


def main():
    number = int(input("Give a number: "))
    poweroftwo(number)


main()
