# author: @shannonmcdermitt

import csv

# turn CSV into dictionary
with open('love.csv') as f:
    reader = csv.DictReader(f)
    words = list(reader)
    
    # convert syllable #'s into integers
    for w in words:
        w['syllables'] = int(w['syllables'])
        print(w['syllables'])
    
    # print only words with 'love' as topic
    for w in words:
        if w['topic'] == 'love':
            print(w['word'])
    
    # print only words with 'space' as topic
    for w in words:
        if w['topic'] == 'space':
            print(w['word'])
    
    # print words with 2 syllables
    for w in words:
        if w['syllables'] == 2:
            print(w['word'])
    
    