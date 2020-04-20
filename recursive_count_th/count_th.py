'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base Case
    # If the word is less than 2 letters, there is no way that 'th' is in it; thus, we set it to 0
    if len(word) < 2:
        return 0

    # Check if first two letters of the word are 'th'; if true, return 1 and then we recurse
    elif word[0] == 't' and word[1] == 'h':
        return 1 + count_th(word[1:]) # to the left of 2nd letter
        
    # If the first two letters are not 'th', we recurse again
    else:
        return count_th(word[1:])
