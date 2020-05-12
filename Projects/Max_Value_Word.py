x = 'man i need a taxi up to ubud'

#This solution assigns a value to each character based off it's position within
#the alphabet. The word with the max sum of character values is returned.

import numpy as np

def high(x):
    #Split the words on the space within the sentence.
    words=x.split(' ')
    
    #Create an empty list
    score_list = []
    
    #Loop through the list of words to determine the score and append the empty 
    #list.
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        score_list.append(scores)
    return words[score_list.index(max(score_list))]


print(high(x))