# CS 301 In-class Assignment Week 1:
# Write the names of your group members (1 on each line) as comments below:
# (Example) Member 1: Hammad Mazhar 


## Question 1: Find the sum of the first n positive integers. 
## Return the result of the sum as an integer
def find_n_sum(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n+find_n_sum(n-1)
print(find_n_sum(5))

## Question 2: Given a proposed word (as the string proposed_word),
## find out if that word is a valid word to play.
## Assume that a text file 'words.txt' is provided in the same directory as this script.
## Return a boolean where 'True' indicates valid word, while 'False' indicates the opposite.
def isValidWord(proposed_word):
    with open(file='words.txt') as words:
        for word in words:
            if word.strip().lower()== proposed_word.strip().lower():
              return True
    return False
    
print(isValidWord('aardvark'))

## Question 3: Given a proposed word (as the string proposed_word)
## and a set of letter tiles (as the list of chars tiles)
## determine if the word can be formed from the given tiles
## Return a boolean indicating yes or no accordingly.
def isWordPossible(proposed_word, tiles):
    if isValidWord(proposed_word):
        temp=0
        for i in proposed_word:
            if tiles[temp]
    else:
        return False

        
print(isWordPossible('abacas',['a','a','b','a','c','s']))
## Question 4: Given a set of letter tiles (as the list of chars tiles)
## determine all possible, valid words that can be formed from those tiles
## Return all possible words as a list.
def allPossibleWords(tiles):
    return

## Question 5: Given a set of outer letters (as the list of chars outer_letters)
## and the center letter (as the char center_letter) for a Spelling Bee puzzle,
## find all possible valid words that can be formed following the Spelling Bee rules.
def spellingBee(outer_letters):
    return

## Question 6: Find a set of 8 letters that gives the most bingoes. 
## Use the given words.txt file as the source of words.
## Return the letters as a list of characters.
def maxBingo():
    return