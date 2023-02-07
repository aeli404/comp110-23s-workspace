"""EX01 - Chardle - We got Worldle at home"""
__author__ = "730576293"

input_5: str = input("Enter a 5-Character word: ")
char_matches: int =0

if len(input_5) != 5:
    print("Error: Word must contain 5 characters")
else:
    input_char: str = input("Enter a single character: ")
    if len(input_char) != 1:
        print("Error: Character must be a single character.")
    else:
        print("Searching for " + input_char + " in " + input_5)

        if input_char == input_5[0]:
            print(input_char + " found at index 0")
            char_matches = char_matches + 1

        if input_char == input_5[1]:
            print(input_char + " found at index 1")
            char_matches = char_matches + 1

        if input_char == input_5[2]:
            print(input_char + " found at index 2")
            char_matches = char_matches + 1

        if input_char == input_5[3]:
            print(input_char + " found at index 3")
            char_matches = char_matches + 1

        if input_char == input_5[4]:
            print(input_char + " found at index 4")
            char_matches = char_matches + 1

        if char_matches == 0:
            print("No instances of " + input_char + " found in " + input_5)
        if char_matches == 1:
            print("1 instance of " + input_char + " found in " + input_5)
        if char_matches > 1:
            char_matches = str(char_matches)
            print(char_matches + " instances of " + input_char + " found in " + input_5)