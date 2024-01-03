def words():
    while True:
        words = input("Enter a string: ")

        if words.replace(" ", "").isalpha():
            reversed_text = words[::-1]
            print("Output:", reversed_text)
            break
        else:
            print("Error Reported! Enter text only.")
            print()

words()