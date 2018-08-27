# Problem_6.py
# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def string_compression(word):
    if len(word) == 1:
        return word + "1"
    else:
        compressed = ''
        count = 0
        while len(word) != 0:
            l, word = word[0], word[1:]
            if compressed == '':
                compressed += l 
                count += 1
            elif l not in compressed[-1]:
                compressed += str(count) + l 
                count = 1          
            else:
                count += 1
        compressed += str(count)
        return compressed

def main():
    print("orginal: {} | Compressed: {}".format('aabcccccaaa', string_compression('aabcccccaaa')))
    print("orginal: {} | Compressed: {}".format('aaaaddsseeabcccccaaa', string_compression('aaaaddsseeabcccccaaa')))
    print("orginal: {} | Compressed: {}".format('hhhggggssstststssssgggeee', string_compression('hhhggggssstststssssgggeee')))
    print("orginal: {} | Compressed: {}".format('lmlmlmfffffggggttttttttssdsds', string_compression('lmlmlmfffffggggttttttttssdsds')))

main()