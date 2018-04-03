def main():
    userInput = input('Welcome.\nEnter Text to see the Pig Latin Version. ')
    firstLetter = userInput[:1]
    newString = userInput.replace(userInput[1:], "")
    evenNewerString = (newString+"-"+(firstLetter)+"ay")
    print(" Even Newer String = "+str(evenNewerString));
               # 0 , 1 , 2, 3 , 4  ,5 
    vowelList =["a","e","i","o","u","y"]
    count = 0
    realFirstLetterIndex =""
    while(count < len(userInput)):
        vowelA = userInput.find(str(vowelList[0]));
        vowelE = userInput.find(str(vowelList[1]));
        vowelI = userInput.find(str(vowelList[2]));
        vowelO = userInput.find(str(vowelList[3]));
        vowelU = userInput.find(str(vowelList[4]));
        vowelY = userInput.find(str(vowelList[5]));

        count+=1
        if vowelA >= 0:
            realFirstLetterIndex = vowelA
        el   if vowelE >= 0:
            realFirstLetterIndex = vowelE
        elif vowelI >= 0:
            realFirstLetterIndex = vowelI
        elif vowelO >= 0:
            realFirstLetterIndex = vowel0
        elif vowelU >= 0:
            realFirstLetterIndex = vowelU
        elif vowelY >= 0:
            realFirstLetterIndex = vowelY
        else:
            realFirstLetterIndex = ""

        print(realFirstLetterIndex);
main()
