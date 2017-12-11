# you need to pip install emoji the way you'd import bs4 via command line
# i just think the emojis are really cute and can't help myself
# import statements
import emoji
from sys import exit

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
    guess method checks 
    def guess(self):
        guess = input('Guess the secret word: ')
        if guess != 'hotdog':
            self.lives = self.lives - 1
            print(self.name + ', you have ' + str(self.lives) + ' lives left.')
        elif guess == 'hotdog':
            print(self.name + ', you won!')
            print(emoji.emojize(':sparkling_heart: :star: :sparkling_heart: :star: :sparkling_heart:', use_aliases=True))
            playAgain()
        if self.lives == 0:
            print('Sorry, ' + self.name + ' you died.')
            playAgain()

# play function gives users the opportunity to have 3 guesses
# the for loop regulates this
def play():
    user = User(input('Hello friend, what is your name? '))
    lives = 3
    user.death(lives)
    for i in range(3):
        user.guess()

# play again allows user to determine whether they want to play again
def playAgain():
    playAgain = input('Do you want to play again? y or n? ').lower()
    if playAgain == 'y':
        play()
    if playAgain == 'n':
        print('See you later.')
        exit()
play()