import random

tie = 0
rounds = 0
won_rounds = 0
while True:
    user_answer = input("Foot, Nuke or Cockroach? (Quit ends): ")
    if user_answer != "Quit" and user_answer == "Foot" or user_answer == "Nuke" or user_answer == "Cockroach":
        print("You chose: ", user_answer)
        computer_answer = random.randint(1, 3)
        if user_answer == "Foot":
            if computer_answer == 1:
                print("Computer chose: Foot")
                print("It is a tie!")
                tie = tie + 1
                rounds = rounds + 1
            elif computer_answer == 2:
                print("Computer chose: Nuke")
                print("You LOSE!")
                rounds = rounds + 1
            elif computer_answer == 3:
                print("Computer chose: Cockroach")
                print("You WIN!")
                rounds = rounds + 1
                won_rounds = won_rounds + 1
        elif user_answer == "Nuke":
            if computer_answer == 1:
                print("Computer chose: Foot")
                print("You WIN!")
                rounds = rounds + 1
                won_rounds = won_rounds + 1
            elif computer_answer == 2:
                print("Computer chose: Nuke")
                print("Both LOSE!")
                rounds = rounds + 1
                tie = tie + 1
            elif computer_answer == 3:
                print("Computer chose: Cockroach")
                print("You LOSE!")
                rounds = rounds + 1
        elif user_answer == "Cockroach":
            if computer_answer == 1:
                print("Computer chose: Foot")
                print("You LOSE!")
                rounds = rounds + 1
            elif computer_answer == 2:
                print("Computer chose: Nuke")
                print("You WIN!")
                rounds = rounds + 1
                won_rounds = won_rounds + 1
            elif computer_answer == 3:
                print("Computer chose: Cockroach")
                print("It is a tie!")
                rounds = rounds + 1
                tie = tie + 1
        else:
            print("Incorrect selection.")
    elif user_answer == "Quit":
        print("You played ", rounds, " rounds, and won ", won_rounds, " rounds, playing tie in ", tie, " rounds.")
        break
    else:
        print("Incorrect selection.")
