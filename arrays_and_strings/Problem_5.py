# Problem_5.py
# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

def ifOneAway(orig, word):
    # test if length is more then 1 from orig
    if len(word) > len(orig)+1 or len(word) < len(orig)-1:
        return False
    # test for if delted a char
    edits = 0
    if len(word) > len(orig) or len(word) < len(orig):
        edits += 1
    # compare each word char by char
    #   if difference is more then 1 return false else true
    for l in word:
        if l in orig and edits < 2:         
            pass
        elif edits >= 2:
            return False
        else:
            edits += 1   
    return True

def main():
    print("{}, {} -> {}".format('pale', 'ple', ifOneAway('pale', 'ple')))
    print("{}, {} -> {}".format('pales', 'pale', ifOneAway('pales', 'pale')))
    print("{}, {} -> {}".format('pale', 'bale', ifOneAway('pale', 'bale')))
    print("{}, {} -> {}".format('pale', 'bake', ifOneAway('pale', 'bake')))
    

main()


