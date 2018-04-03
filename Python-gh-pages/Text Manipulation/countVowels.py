def main():
    userInput = input('Welcome.\nEnter Text to count the number of vowels.')
    userInputLower = userInput.lower()
    vowelA = userInputLower.count('a')
    vowelE = userInputLower.count('e')
    vowelI = userInputLower.count('i')
    vowelO = userInputLower.count('o')
    vowelU = userInputLower.count('u')
    vowelY = userInputLower.count('y')
    totalVowelCount = (vowelA)+(vowelE)+(vowelI)+(vowelO)+(vowelU)+(vowelY)
    print("There are " +(str(totalVowelCount)) + " vowels.");
    print((str(vowelA)) + " A's.");
    print((str(vowelE)) + " E's.");
    print((str(vowelI)) + " I's.");
    print((str(vowelO)) + " O's.");
    print((str(vowelU)) + " U's.");
    print((str(vowelY)) + " Y's.");
#def secondMain():
 #   vowelsList = ['a','e','i','o','u','y']
  #  userInput = input('Welcome.\nEnter Text to count the number of vowels.')
   # userInputLower = userInput.lower()

    #count = 0
    #countTwo = 0
    #while count < len(userInputLower):
     #   count+=1
      #  if userInputLower[count]== vowelsList[count]:
       #     countTwo+=1
    #print(countTwo)
   # print("Number of times a vowel appears: "+(str(countA)));
    

main()
