'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    def count_th_recursion(word, start):
        # This function sees if 'word' starts with 'th' beginning at position 'start',
        # then adds 1 to 'start' and repeats.
        if start == len(word):
            # Base case: If we've reached the end of the word, it obviously can't
            # start with 'th', so just return 0.
            return 0
        count = word.startswith('th', start)
        # The 'startswith' method returns True if 'word' begins with the specified
        # string ('th' in this case) at position 'start', and False if it doesn't.
        # Since Python interprets booleans as numbers, that means count will be 1
        # if startswith is True, and 0 if it's False.
        return count + count_th_recursion(word, start+1)
        # Run the function again, adding 1 to 'start' so we check the next location.

    return count_th_recursion(word, 0)
    # Run the above recursive function starting at location 0.
