# hangman in python
from words import words_list
import random
import sys

random_word = random.choice(words_list).lower()
random_word_lst = list(random_word)
run = True

def draw_hang(lives):
    if lives == 5:
        print("|")
        print("|")
        print("|")
        print("|")
    if lives == 4:
        print("|------")
        print("|")
        print("|")
        print("|")
    if lives == 3:
        print("|------")
        print("|      |")
        print("|")
        print("|")
    if lives == 2:
        print("|------")
        print("|      |")
        print("|      O")
        print("|")
    if lives == 1:
        print("|------")
        print("|      |")
        print("|      O")
        print("|     /|\ ")
    if lives == 0:
        print("|------")
        print("|      |")
        print("|      O")
        print("|     /|\ ")
        print("      / \ ")
        print("You have lost!")
        print(" ".join(random_word_lst))
        sys.exit()

def loop():
    gaps = []
    count = -1
    lives = 6
    count1 = -1
    found_letters = list()
    for letter in random_word_lst:
        count += 1
        gaps.append(letter)
        gaps[count] = "_"
    while run:
        count1 = -1
        print(" ".join(gaps))
        guess = input("Guess a letter: ")
        if guess in random_word_lst:
            for letter in random_word_lst:
                count1 += 1
                if random_word_lst[count1] == guess and gaps[count1] == "_":
                    found_letters.append(random_word_lst[count1])
                    gaps[count1] = guess
                if len(random_word_lst) == len(found_letters):
                    print("You have won!")
                    print(" ".join(gaps))
                    sys.exit()


        elif guess not in random_word_lst:
            lives -= 1
            draw_hang(lives)


loop()


