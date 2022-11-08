# hw for meeting 2/18/21
# advent of code day 25, diffie hellman application



def transform(subjectNum, loopSize):
    value = 1
    for i in range(0, loopSize):
        value = (value * subjectNum)%20201227
    return value
def oldGetLoopSize(publicKey):
    loopSize = 1
    while (transform(7, loopSize) != publicKey):
        print(loopSize)
        loopSize+= 1
    return loopSize

def getLoopSize(publicKey):
    loopSize = 0
    transformed = 1

    while transformed != publicKey:
        loopSize += 1
        transformed = (transformed * 7) % 20201227
    return loopSize

def getEncryptionKey(loopSize, publicKey):
    return transform(publicKey, loopSize)


def  main():
    cardPublicKey = 6930903
    doorPublicKey = 19716708
    cardLoopSize = getLoopSize(cardPublicKey)
    print(cardLoopSize)
    print(transform(7, cardLoopSize), cardPublicKey)
    doorLoopSize = getLoopSize(doorPublicKey)
    print(doorLoopSize)
    print(getEncryptionKey(cardLoopSize, doorPublicKey))
    print(getEncryptionKey(doorLoopSize, cardPublicKey))

main()
