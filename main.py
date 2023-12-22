import random

# Title
print(""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
""")
print(f"\033[1m{'HANGMAN GAME':^47}\033[0m")
print("-" * 47)

# lists and count of errors
word_list = ["ardvark", "baboon", "camel", "rabbit", "donkey", "cheetah", "squirrel", "pig", "elephant", "horse",
             "giraffe", "cow", "lion", "deer", "bear", "goat", "zebra", "cat", "dog", "cockatiel", "mouse"]
chosen_word = random.choice(word_list)
display = list("_" * len(chosen_word))
errors = 0
stage = 6
guessed = ''

#

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Game code
while True:

    if errors > 6:
        print("~~~ You lose! ~~~")
        break
    elif "_" not in display:
        print("~~~ You Win! ~~~")
        break

    print(stages[stage])
    guess = str(input("-> Guess a letter: ")).lower()

    if guess in guessed:
        print(f"You've already guessed '{guess}'.")
        continue
    else:
        guessed += guess

    for number, letter in enumerate(chosen_word):
        if letter == guess:
            display[number] = letter

    if guess not in chosen_word:
        errors += 1
        print(f"- You guessed '{guess}', that's not in the word. You lose a life. -")
        stage -= 1
        if stage > -1:
            print(f"You have more {stage + 1} chance(s).")

    print(display)
