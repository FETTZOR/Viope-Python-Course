while True:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit")

    select = int(input("Please select one: "))
    print()

    if select == 1:
        file = open("notebook.txt", "r")
        file_text = file.read()
        print(file_text)
        file.close()

    elif select == 2:
        file = open("notebook.txt", 'a')

        text_for_file = input("Write a new note: ")
        file.write(text_for_file)

        file.close()

    elif select == 3:
        file = open("notebook.txt", 'w')
        file.close()
        print("Notes deleted.")
    elif select == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Wrong input")