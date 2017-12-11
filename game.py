import os, time, random, csv
import emoji
from sys import exit
import pandas as pd
import io

class User(object):
    """
    This class creates a User object. The only parameter that needs to be passed is a name. This can be done with an input statement to collect the user's name to use throughout the program.
    """
    def __init__(self, name):
        self.name = name

    # death method regulates player lives
    def death(self, lives):
        self.lives = lives
    
    # this is a simple guess the keyword game
    # users supply the guess through input
    # the guess input is checked against the conditions
    # to see if it matches the secret word
    # the secret word is hotdog
    # if a user guesses wrong a life is taken
    def poem(self):
        line1 = [input('LINE 1: ').lower()]
        with open('love.csv') as csvfile:
            header = csvfile.next()
            total = 0
            for row in csv.reader(csvfile):
                total += int(row[1])
            print(total)
            
#        if guess != 'hotdog':
#            self.lives = self.lives - 1
#            print(self.name + ', you have ' + str(self.lives) + ' lives left.')
#        elif guess == 'hotdog':
#            print(self.name + ', you won!')
#            print(emoji.emojize(':sparkling_heart: :star: :sparkling_heart: :star: :sparkling_heart:', use_aliases=True))
#            playAgain()
#        if self.lives == 0:
#            print('Sorry, ' + self.name + ' you died.')
#            playAgain()

# open csv to read
reader = csv.reader(open('love.csv', 'r'))

love = list(zip(*reader))[0][1]
#space = list(zip(*reader))[0][39]

def wordbank():
    # open csv to read
    reader = csv.reader(open('love.csv', 'r'))
    
    # only pulls from word colum
    # keep in mind csv is zero indexed
    col2 = list(zip(*reader))[1]
    
    # range of 20 words
    for i in range(20):
        print(random.choice(col2))
    
# play function gives users the opportunity to have 3 guesses
# the for loop regulates this
def play():
    user = User(input('Hello friend, what is your name? '))
    print('')
    wordbank()
    lives = 3
    user.death(lives)
    for i in range(3):
        user.poem()

# play again allows user to determine whether they want to play again
def playAgain():
    playAgain = input('Do you want to play again? y or n? ').lower()
    if playAgain == 'y':
        play()
    if playAgain == 'n':
        print('See you later.')
        exit()

# list of instructions for player
def instructions():
    print("\nYou must create a haiku poem within the designated time limit.")
    print("\n60 seconds for easy, 45 seconds for medium, and 30 seconds for hard.")
    print("\nWhen your time is up a beep will sound and TIME IS UP will display on screen.")
    print("\nIf you fail to complete the haiku in time, you will lose a life!")
    print("\nLose 3 lives and it's game over!")

# option to choose level of difficulty
def options():
    b = 0
    # while loop creates avenue to close program
    while b == 0:
        choice = input("Press 1 for easy, 2 for medium, 3 for hard, or 4 to exit: ")
        if choice == "1":
            play()
            print('EASY')
            timer(60)
        elif choice == "2":
            play()
            print('MEDIUM')
            timer(45)
        elif choice == "3":
            play()
            print('HARD')
            timer(10)
        elif choice == "4":
            print("Goodbye")
            b = 1
        else:
            print("Please press 1 for easy, 2 for medium, 3 for hard, or 4 to exit:")

# timer function 
# pass amount of time in seconds as argument in timer param
# beep sourced from stack overflow because winsound isn't an option
def timer(n):
    beep = lambda x: os.system("echo TIME IS UP '\a';sleep 0.2;" * x)
    while n > 0:
        n = n -1
        time.sleep(1)
        if n ==0:
            beep(1)
            break
# welcome message
def welcome():
    print("\nWelcome to our Haiku puzzle extravaganza!")
    instructions()
    options()
    

welcome()