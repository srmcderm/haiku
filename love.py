import csv
import os
import emoji
#Sourced from https://github.com/carpedm20/emoji

# YOU NEED TO PIP INSTALL EMOJI TO SEE THE EMOJIS

#open file
fh = open('love.csv', 'a')

print('If in command line, PRESS ctrl-c to quit.')
print(emoji.emojize(':heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart:', use_aliases=True))
print('THIS PROGRAM ALLOWS YOU TO UPLOAD WORDS TO A CSV FILE.')
print(emoji.emojize(':heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart:', use_aliases=True))
print('THE THEME IS LOVE, IF THAT WASN\'T OBVIOUS.')
print('')

# check to see if file is empty so we know when to write header
fileEmpty = os.stat('love.csv').st_size == 0


with open('love.csv', 'a', newline='') as csvfile:
            
    headers = ['topic', 'word', 'syllables']
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)
        
    # only write header once
    if fileEmpty:            
        writer.writeheader()
    for i in range(1000):    
        writer.writerow({
            'topic':'space',
            'word':input('WORD: '),
            'syllables':input('SYLLABLES: ')})
    fh.close()