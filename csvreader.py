# author: @shannonmcdermitt

import csv

# turn CSV into dictionary
with open('love.csv') as f:
    reader = csv.DictReader(f)
    words = list(reader)
    
    print('-'*20)
    # convert syllable #'s into integers
    for w in words:
        w['syllables'] = int(w['syllables'])
        print(w['syllables'])
    
    print('-'*20)
    # print only words with 'love' as topic
    for w in words:
        if w['topic'] == 'love':
            print(w['word'])
    
    print('-'*20)
    # print only words with 'space' as topic
    for w in words:
        if w['topic'] == 'space':
            print(w['word'])
    
    print('-'*20)
    # print words with 1 syllable
    for w in words:
        if w['syllables'] == 1:
            for i in w['word']:
                oneWord = w['syllables']        
            print(w['word'])
    
    print('-'*20)
    # print words with 2 syllables
    for w in words:
        if w['syllables'] == 2:
            for i in w['word']:
                twoWord = w['syllables'] 
            print(w['word'])
            
    print('-'*20)
    # print words with 2 syllables
    for w in words:
        if w['syllables'] == 3:
            for i in w['word']:
                threeWord = w['syllables'] 
            print(w['word'])
    
    # syllable set variables
    # all of these equal five
    set1 = oneWord + oneWord + oneWord + oneWord + oneWord
    set2 = oneWord + twoWord + twoWord
    set3 = oneWord + oneWord + oneWord + twoWord
    set4 = twoWord + threeWord
    
    userList = []
    userLine1 = input('LINE 1: ').lower()
    splitLine1 = userLine1.split()
    userList.append(splitLine1)
    
#    if userList == set1:
#        print('Great')
#    elif userList == set2:
#        print('Great')
#    elif userList == set3:
#        print('Great')
#    elif userList == set4:
#        print('Great')
#    else:
#        print('Oops')
#    print(userList)
#    
#    line2 = 7
#    line3 = 5
#    userLine2 = input('LINE 2: ')
#    userLine3 = input('LINE 3: ')
#    
#    
    
#    