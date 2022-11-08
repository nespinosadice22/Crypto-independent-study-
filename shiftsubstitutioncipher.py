# shift substitution cipher

f = open('ciphertext1.txt','r')
letter = f.readlines()[0]

def main():
    frequency = {'E': 13.11, 'T': 10.47, 'A': 8.15}
    codeLetters = {'A':'','B':'', 'C':'','D':'','E':'','F':'', 'G':'','H':'','I':'','J':'','K':'','L':'','M':'','N':'','O':'','P':'','Q':'','R':'','S':'','T':'','U':'','V':'','W':'','X':'','Y':'','Z':''}
    numLetters = {'A':0,'B':0, 'C':0,'D':0,'E':0,'F':0, 'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    shiftLetters = {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '',
                   'L': '', 'M': '', 'N': '', 'O': '', 'P': '', 'Q': '', 'R': '', 'S': '', 'T': '', 'U': '', 'V': '',
                   'W': '', 'X': '', 'Y': '', 'Z': ''}
    for i in range(0,len(letter)):
        n = letter[i].upper()
        numLetters[n] +=1
    max = "A"
    print(numLetters)
    for i in numLetters:
       if numLetters[i] > numLetters[max]:
           max = i
    print("max", max)
    shiftLetters[max] = "E"
    shift = ord(max) - ord("E")
    # original letter + 11 = shifted letter
    for i in shiftLetters:
        if (ord(i)-11) < 65:
            shiftLetters[i] = chr(ord(i)-11+26)
        else:
            shiftLetters[i] = chr(ord(i) - 11)
        print(i, shiftLetters[i])
    decryptedLetter = ''
    for i in range(0, len(letter)):
        upperLetter = letter[i].upper()
        decryptedLetter = decryptedLetter + shiftLetters[upperLetter]
    print(decryptedLetter)


main()