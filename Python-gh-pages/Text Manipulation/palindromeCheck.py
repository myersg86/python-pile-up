def main():
    print("Welcome.\nThis program will determine if a given value is a palindrome.")
    userText = str(input('Please Enter a Word:\n'))
    userText2 = userText.lower()
    if(str(userText2)==(str(userText2)[::-1])):
        print("Yes. "+userText+" is a Palindrome.")
    elif(str(userText2)!=(str(userText2)[::-1])):
        print("No. "+userText+" is NOT a Palindrome.")
main()
