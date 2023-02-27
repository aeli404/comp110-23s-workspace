"""EX02 - One shot Wordle - the sequel."""
__author__ = "730576293"

secret_word = "python"
len_check = False
ind_check = 0
result_em = ""
white_box = "\U00002B1C"
green_box = "\U0001F7E9"
yellow_box = "\U0001F7E8"

# retrives user guess
user_guess = input(f"What is your {len(secret_word)}-letter guess? ")

# checks for correct length
while len_check is not True:
    if len(user_guess) == len(secret_word):
        len_check = True
    else:
        user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

# checks indices for matches, and if no match checks for that character in the secret word
# adds approprate color block when done & prints
while ind_check < len(secret_word):
    if user_guess[ind_check] == secret_word[ind_check]:
        result_em = result_em + green_box
    else:
        loc_check = False
        loc_ind_check = 0
        while loc_check is False and loc_ind_check < len(secret_word):
            if secret_word[loc_ind_check] == user_guess[ind_check]:
                loc_check = True
            else:
                loc_ind_check = loc_ind_check + 1
        if loc_check is True:
            result_em = result_em + yellow_box
        else:
            result_em = result_em + white_box
    ind_check = ind_check + 1
print(result_em)

# prints whether guess is completely correct
if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")