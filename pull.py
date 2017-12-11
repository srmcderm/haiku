import csv
import random

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
    topic = input('Select topic: ')
    for i in range(20):
        if love == 'love' and topic == 'love':
            print(random.choice(col2))
#        elif space == 'space' and topic == 'space':
#            print(random.choice(col2))
wordbank()
