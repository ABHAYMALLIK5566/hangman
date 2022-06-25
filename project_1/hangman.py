print("           HANGMAN")
word=["Exclusive","Hound","Scanner","Victory","Patience","Drawing","Worker","Pay","Tomorrow","Acrobatic","Tactic","Stupid","Success"]
stage=[''' 
  +------+
  |      |
  O      |
 /|\     |
 / \     |
   ______|______
''','''
  +------+
  |      |
  O      |
 /|\     |
 /       |
   ______|______
''','''
  +------+
  |      |
  O      |
 /|\     |
         |
   ______|______
''','''
  +------+
  |      |
  O      |
 /|      |
         |
   ______|______
''','''
  +------+
  |      |
  O      |
 /       |
         |
   ______|______
''','''
  +------+
  |      |
  O      |
         |
         |
   ______|______
''','''
  +------+
  |      |
         |
         |
         |
   ______|______


''']

import os
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

import random
chosen_word=random.choice(word).lower()
display=[]
for _ in chosen_word:
    display += "_"
print(display)
lives = 6
num = len(stage)
not_false = True

while not_false:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print("You've already choosen the word.")
    for position in range(len(chosen_word)):
        wrd = chosen_word[position]
        if wrd == guess:
            display[position] = wrd
    if guess not in chosen_word:
        print(f"'{guess}' not in that word. You lose a life.")
        lives -= 1
        num -= 1
    print(display)
    print(stage[num - 1])
    if "_" not in display:
        not_false = False
        print("Congratulations, You won!🌟")
    elif lives == 0:
        print(f"Your all lives are finished. The word was '{chosen_word}'")
        not_false = False
        print("You lose!💣")

