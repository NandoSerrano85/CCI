# Problem_2.py
# Given two strings, write a method to decide if one is a permutation of the other.

def premutation_check(word1, word2):
    # 1st step remove empty space
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")

    # test for equal length
    if len(word1) != len(word2):
        return False

    # 2nd step split into characters
    word1 = list(word1)
    word2 = list(word2)

    # 3rd step sort each word
    word1.sort()
    word2.sort()
    #loop through and make comparisons
    for n in range(0, len(word1)):
        if word1[n] != word2[n]:
            return False
    return True

def main():
    print("word 1: dog\tword 2: god\tpermutation: {}".format(premutation_check('dog','god')))
    print("word 1: 'dog      '\tword 2: god\tpermutation: {}".format(premutation_check('dog      ','god')))
main()