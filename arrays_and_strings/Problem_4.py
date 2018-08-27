# Problem_4.py
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.

# in order to generate all permutation importedt this library
from itertools import permutations

# Check if string is palindrome
# return bool, string with the letters to be used, the middle char, positions of blank spaces
def check(word):
    isPal = False
    charCount = dict()
    blanks = list()
    letters = ''
    middle = ''
    for n in range(0,len(word)):
        if word[n] != ' ':
            try:
                charCount[word[n]] += 1
            except:
                charCount[word[n]] = 1
        else:
            blanks.append(n)
    for k,v in charCount.items():
        if v%2 == 1:
            if isPal:
                return False, '', '', []
            isPal = True
            middle = k
        elif v > 2:
            num = int(v/2)
            for n in range(0,num):
                letters += k
        else:
            letters += k

    return isPal, letters, middle, blanks


# generate permutations of palindrome
# return bool, list of palindrome permutations
def palindrome_permutation(word):
    word = word.lower()
    perm_list = list()
    pal, letters, mid, blanks = check(word)
    if pal:
        perms = [''.join(p) for p in permutations(letters)]
        for p in perms:
            words = p + mid + p[::-1]
            for b in blanks:
                words = words[:b] + " " + words[b:]
            perm_list.append(words)
        return pal, perm_list
    else:
        return pal, perm_list

def main():
    found, results = palindrome_permutation("Tact Coa")
    print("{} ({})".format(found, results))
main()