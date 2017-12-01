# question 6

def asearch(l,key,ida=0):
    if l:   # checks if list exists
        if l[0] == key:     
            return ida
        s = asearch(l[1:], key, (ida + 1))      # recursion
        if s is not False:          
            return s
        #### if s is flase it will return false ####
        #### so it can return s unconditionally!                   ####
    return False            # returns false if key not found

def bsearch(l,key,ida=0):
    if l:   # checks if list exists
        if l[0] == key:     
            return ida
        return bsearch(l[1:], key, (ida + 1))      # recursion
    return False            # returns false if key not found
    #### above statement is better put closer to the `if` ####

def csearch(l,key,ida=0):
    if not l:   # checks if list exists
        return False
    if l[0] == key:     # base case - first index is key
        return ida
    return zsearch(l[1:], key, (ida + 1))      # recursion

