"""EXO3 - Structured Worldle"""
__author__ = "730576293"

"""A function that searches for a character(char g) inside a string(search_str).
Returns answer as a bool"""
def contains_char(search_str: str,char_g: str) -> bool:
  assert len(char_g) == 1
  ind_check = 0
  contains = False
  while contains is False and ind_check < len(search_str):
    if search_str[ind_check] == char_g:
      contains = True
    else:
      ind_check = ind_check + 1
  return contains

"""A function that when given the secret and key words(of the same length) returns a string of emojis repersenting how accurate
the guess string is to the secret string. The contains_char function is used to determine if a character in the guess is in the 
secret word at any index besides the correct one."""
def emojified(user_guess: str,secret_word: str) -> str:
  assert len(user_guess) == len(secret_word)
  white_box = "\U00002B1C"
  green_box = "\U0001F7E9"
  yellow_box = "\U0001F7E8"
  ind_check = 0
  result_em = ""
  while ind_check < len(secret_word):
    if user_guess[ind_check] == secret_word[ind_check]:
      result_em = result_em + green_box
    else:
      if contains_char(secret_word,user_guess[ind_check]) == True:
        result_em = result_em + yellow_box
      else:
        result_em = result_em + white_box
    ind_check = ind_check + 1
  return result_em

"""A function that asks for an expected length of the secret word & guesses(expected_len) and asks for user guesses until they 
match the length expected. When that happens, the correct length guess is returned."""
def input_guess(expected_len: int) -> str:
  user_guess: str = input(f"Enter a {expected_len} character word: ")
  while len(user_guess) != expected_len:
    user_guess: str = input(f"That wasn't {expected_len} chars! Try again: ")
  return user_guess


"""Main, a funtion that comntrols the whole game. Sets input_guess in a while
loop until 6 failed tries or sucesfully guessing the secret word"""
def main() -> None:
    secret_word = "codes"
    expected_len = len(secret_word)
    turn = 1
    win_stat = False
    while turn < 7 and win_stat == False:
        print(f"=== Turn {turn}/6 ===")
        user_guess = input_guess(expected_len)
        if user_guess == secret_word:
            win_stat = True
            print(emojified(user_guess,secret_word))
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
            print(emojified(user_guess,secret_word))
        if turn == 7 and win_stat == False:
            print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()