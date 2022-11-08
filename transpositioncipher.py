
#transposition cipher encryption and decryption
#note: enter messages without spaces, assuming 25 letter message
def main():
    string =input("Enter message: ")
    key = input("Decrypt or encrypt?: ").lower()
    if key == "encrypt":
        if len(string) > 25:
            string = string[0:25]
        list = []
        rowList = []
        for i in range(0, 25):
            rowList.append(string[i])
            if ((i+1)%5)==0:
                list.append(rowList)
                rowList = []
        print(list)
        stringList = []
        string1 = ''
        for i in range(0, 5):
            for x in range(0, 5):
                string1 = string1 + list[x][i]
            stringList.append(string1)
            string1 = ''
        for i in range(0, 5):
            print(stringList[i], end = "")
    else:
        stringList = []
        stringA = ''
        for i in range(0, 5):
            stringA = string[i] + string[i+5]+ string[i+10] + string[i+15] + string[i+20]
            stringList.append(stringA)
        for i in range(0, 5):
            print(stringList[i], end = "")


main()


'''
example: encrypt "four score and seven years ago our fathers" (don't use spaces) --> fcneroodnsursyareeegsavao
example: decrypt "WNOOAHTUFNEHRHENESUVICEME" --> "WHEN IN THE COURSE OF HUMAN EVE" 

'''


