'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

'''
We are looking to find how often the letters 'th' appear in a word
For example the word 'with' has it occur once, whereas the word 'subtle' has none
Case matters so if the word passed in is 'Thinker' this would have zero
or if you want to get cheeky the word 'wiTh' has zero as well
No loops, must work with recursion.
'''

def count_th(word):
    # get length of word
    n = len(word)
    # set a variable to keep track of counts
    i = 0
    # if there is 1 of fewer letters left
    if n <= 1:
        # return 0
        return 0
    # if the first two letters are th
    if word[:2] == 'th':
        # increment i
        i += 1
        # recurse without the two letters
        i += count_th(word[2:])
    # else rucurse without the first letter
    else:
        i += count_th(word[1:])
    
    return i
