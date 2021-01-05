def test(input_sentence):
    if input_sentence == 'quit':
        print('quit')
        return False
    elif len(input_sentence) < 10 and input_sentence != "quit":
        print("Too short")
        return True
    elif len(input_sentence) > 10:
        print(input_sentence)
        return True
    else:
        print("strange input")
        return True


def main():
    exec_guard = True
    while exec_guard:
        input_sentence = input("Write something (quit ends):")
        exec_guard = test(input_sentence)


if __name__ == "__main__":
    main()
