import base64

def XOR(str1, str2):
    binAnswer = ''
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            binAnswer = binAnswer + '1'
        else:
            binAnswer = binAnswer + '0'
    return (binAnswer)

def hamming(str1, str2):
    check1 = ''
    check2 = ''
    for i in range(0, len(str1)):
        bin1 = ord(str1[i])
        bin1 = bin(bin1)
        bin1 = bin1[2:]
        while len(bin1) < 8:
            bin1 = "0" + bin1
        bin2 = ord(str2[i])
        bin2 = bin(bin2)
        bin2 = bin2[2:]
        while len(bin2) < 8:
            bin2 = "0" + bin2
        check1 += bin1
        check2 += bin2
    x = XOR(check1, check2)
    return (x.count("1"))

#print(hamming("this is a test", "wokka wokka!!!"))

def singleXORcipher(decoded, charval):
    output = b''
    #decoded = bytes.fromhex(s)
    for byte in decoded:
        output += bytes([byte ^ charval])
    return output, charval

def tryallkeys(s):
    plaintexts = []
    for i in range(256):
        what, intval = singleXORcipher(s, i)
        #print(what)
        try:
            plaintext = what.decode("utf-8")
        except UnicodeDecodeError:
            pass
        else:
            #print('plaintext', plaintext)
            plaintexts.append(plaintext)
    return plaintexts


def englishscore(plaintexts):
    bestkey = -1
    key = 0
    best = ''
    bestscore = 100
    for p in plaintexts:
        p = str(p)
        score = 0
        for ch in p:
            val = ord(ch)
            if val > 122:
                score += 1
            if val < 64 and val != 32:
                score += 1

        if score < bestscore:
            best = p
            bestscore = score
            bestkey = key
        key += 1
    return best, bestkey

def smallestdistance(ciphertext):
    hammingdict = dict()
    for keysize in range(2, 41):
        distances = []
        chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
        numchunks = len(chunks)
        while True:
            try:
                chunk1 = chunks[0]
                chunk2 = chunks[1]
                string1 = ''
                string2 = ''
                for c in chunk1:
                    string1 += chr(c)
                for c in chunk2:
                    string2 += chr(c)
                distance = hamming(string1, string2)
                distances.append(distance/keysize)

                del chunks[0]
                del chunks[0]

            except Exception as e:
                break
        hammingdict[keysize] = sum(distances)/len(distances)
    sorteddict = {k: v for k, v in sorted(hammingdict.items(), key=lambda item: item[1])}
    return sorteddict

def repeatingkeyXORcipher(text, key):
    index = 0
    output = b''
    for byte in text:
        output += bytes([byte ^ key[index]])
        index = (index + 1) % len(key)
    return output

def main():
    f = open('challenge6input.txt')
    contents = f.read()
    ciphertext = base64.b64decode(contents)
    print(ciphertext)

    print(smallestdistance(ciphertext))
    #looks like it's 29, 40, 25

    possible_key_length = 29
    blocks = []
    for i in range(possible_key_length):
        block = b''
        for j in range(i, len(ciphertext), possible_key_length):
            block += bytes([ciphertext[j]])
        #print(block)
        blocks.append(block)

    repeatingkey = ''
    for i in range(len(blocks)):
        plaintexts = tryallkeys(blocks[i])
        foundit, realkey = englishscore(plaintexts)
        repeatingkey += chr(realkey)
    print(repeatingkey)

    finalkey = b'Terminator X: Bring the noise'
    plaintext = repeatingkeyXORcipher(ciphertext, finalkey)
    #print(plaintext)
    print(plaintext.decode('utf-8'))






main()