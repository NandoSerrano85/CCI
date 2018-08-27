# Problem 1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def check_if_all_unique(word):
    temp = ''
    for n in word:
        if n in temp:
            return False
        else:
            temp += n

    return True

def main():
    # for testing
    test_string = 'Is Unique Implement an algorithm to determine if a string has all unique characters What if you cannot use additional data structures'
    words = test_string.split()
    for w in words:
        check = check_if_all_unique(w)
        print(f'Word: {w:18} IS unique? {check}')
main()