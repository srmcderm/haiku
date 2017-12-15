# author: @shannonmcdermitt
# author: @shelbyfoxpurrier
# author: @caracastillo


# TDB ADDED: Added json module here
import os, time, random, csv, collections, json 
import emoji
from sys import exit
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
        
    def csvImport(self):
        input_file = csv.DictReader(open('love.csv'))
        return input_file
        #return dict_list
    
    # TDB ADDED
    def randomWords(self, num):
        self.num = num
        
        listOfWords = []
        words = self.csvImport()
        for row in words:
            listOfWords.append(row['word']) 
    
        listOfWordsRandom = random.sample(listOfWords, num)
        return listOfWordsRandom
    
    def takeGuess(self, i):
        words = self.csvImport() # TDB ADDED: get words
        correctWords = {} # TDB ADDED: set up dictionary for correct words
        sumSyllables = 0 # TDB ADDED: set up to sum syllables
        
        # TDB ADDED: 3 lines
#        for i in range(1,3):
        guess = input('Please enter line #'+str(i)+' of the haiku (separate each word by a space): ')    
        word_guesses = guess.split(' ') # TDB ADDED: split into list
            
        # TDB ADDED: Iterate throu dictionary
        for row in words:
              # TDB ADDED: iterate through input words
            for k,w in enumerate(word_guesses):
                    
                # TDB ADDED: Find a match
                if w == row['word']:
                    # TDB ADDED:  Add syllables count
                    correctWords[row['word']] = int(row['syllables'])
                        
        # TDB ADDED: Do something depending on line of haiku
        if i == 1:
            sumSyllables = sum(correctWords.values()) # TDB ADDED: Sum syllables entered
                
            # TDB ADDED: 5 syllables first line
            if sumSyllables == 5:
                print('Great! That is correct for line #'+str(i))
            else:
                ('Wrong!')
                self.lives = self.lives - 1
                print(self.name + ', you have ' + str(self.lives) + ' lives left.')
                options()
            print('You used ' + str(sumSyllables) + ' syllables')
            print(correctWords)
            
        elif i == 2:
            sumSyllables = sum(correctWords.values()) # TDB ADDED: Sum syllables entered
            if sumSyllables == 7:
                print('Great! That is correct for line #'+str(i))
            else:
                ('Wrong!')
                self.lives = self.lives - 1                   
                print(self.name + ', you have ' + str(self.lives) + ' lives left.')
                options()
            print('You used ' + str(sumSyllables) + ' syllables.')
            print(correctWords)
            
        elif i == 3:
            sumSyllables = sum(correctWords.values()) # TDB ADDED: Sum syllables entered
            if sumSyllables == 5:
                print("Great! That is correct for line #"+str(i))
            else:
                ('Wrong!')
                self.lives = self.lives - 1                   
                print(self.name + ', you have ' + str(self.lives) + ' lives left.')
                options()
            print('You used ' + str(sumSyllables) + ' syllables')
            print(correctWords)
                
            exit()
            
# play function gives users the opportunity to have 3 guesses
# the for loop regulates this

def play():
    user = User(input('Hello friend, what is your name? '))
    print('')
    
    
    #TDB ADDED: Get random words from object
    randomWords = user.randomWords(20)
    print('Choose from the following words:\n')
    for w in randomWords:
        print('\t'+w)
        
    lives = 3
    user.death(lives)
    user.takeGuess(1)
    user.takeGuess(2)
    user.takeGuess(3)
    if lives == 3:
        print('You made it through round one.')
    elif lives == 2:
        print('You lost a life, but that\'s okay.')
    elif lives == 1:
        print('Uh oh, one life left.')
    elif lives == 0:
        print(emoji.emojize('DEATH! :skull: :skull: :skull:',use_aliases=True))
        playAgain()
    
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
    print('\nYou must create a haiku poem within the designated time limit.')
    print('\n60 seconds for easy, 45 seconds for medium, and 30 seconds for hard.')
    print('\nYou cannot repeat words!')
    print('\nWhen your time is up a beep will sound and TIME IS UP will display on screen.')
    print('\nIf you fail to complete the haiku in time, you will lose a life!')
    print('\nLose 3 lives and it's game over!')

# option to choose level of difficulty
def options():
    b = 0
    # while loop creates avenue to close program
    while b == 0:
        choice = input('Press 1 for easy, 2 for medium, 3 for hard, or 4 to exit: ')
        if choice == '1':
            print('EASY')
            print('Your timer starts now. You have 60 seconds.')
            timer(60)
            play()
        elif choice == '2':
            print('MEDIUM')
            print('Your timer starts now. You have 45 seconds.')
            timer(45)
            play()
        elif choice == '3':
            print('HARD')
            print('Your timer starts now. You have 30 seconds.')
            timer(30):
            play()
        elif choice == '4':
            print("Goodbye")
            b = 1
        else:
            print('Please press 1 for easy, 2 for medium, 3 for hard, or 4 to exit:')

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
    print(emoji.emojize('\n:sparkles:Welcome to our Haiku puzzle extravaganza!:sparkles:', use_aliases=True))
    instructions()
    options()

welcome()
instructions()
options()