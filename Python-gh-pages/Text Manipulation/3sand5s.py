def main():
    print("Welcome.\nThis program will display the Summation of the Multitudes of 3 & 5, Up unto a number you choose.")
    userNum = int(input('Please Enter a number\n'))
    three,five = 0,0
    threeArray,fiveArray = [],[]
    
    for val in range(0,userNum,3):
                  three += val
                  threeArray.append(val)

    for val in range(0,userNum,5):
                  five += val
                  fiveArray.append(val)

    numList = threeArray + fiveArray
    print("Sum: "+str(sum(sorted(set(numList))))+".")
                  
main()                
