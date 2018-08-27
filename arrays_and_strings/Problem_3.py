# Problem_3.py
# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

def URLify(item, length):
    # split item to remove all empty spaces
    item = item.split()
    # fill all empty spaces between 0 and n-1 words
    word = ''
    for n in range(0, len(item)):
        if n == len(item)-1:
            word += item[n]
        else:
            word += item[n] + '%20'
    return word

def main():
    print(URLify("Mr John Smith ", 13))
    print(URLify("Write a method to replace all spaces in a ", 42))
main()