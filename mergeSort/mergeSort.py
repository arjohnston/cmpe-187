def merge_Sort(A, B):
    #Merges the two arrays 
    #Sorts merged arrays
    A.extend(B)
    A.sort()
    return A

def checkInput(userInput):
    #Checks if input length > 0
    #Removes spaces from user input
    #Checks if user input is all digits
    #If not, warn user and return false
    #Checks if user input is sorted
    #If not, warn user and return false, otherwise return true
    if(len(userInput) is not 0):
        if(checkDigits(userInput)):
            if(userInput == sorted(userInput)):
                return True
            else:
                print("Please enter sorted array!")
    else:
        print("Please enter an array!")
    return False

def checkDigits(userInput):
    #Loops through each element of input array
    #Strips leading "-" to check if element is digit
    #If digit, convert string to int
    #Otherwise warn user and return false
    for num in range(len(userInput)):
        if(userInput[num].lstrip('-').isdigit()):
            userInput[num] = int(userInput[num])
        else:
            print("Please enter numbers only!")
            return False
    return True

def main():
    checkA = False
    checkB = False

    #Get user input
    #Convert string input into list
    #Check if input is valid
    #Set checkA/checkB to True if input is valid and break out of while loop
    while(not checkA):
        userInput = raw_input("Enter First Array (Leave Spaces Between Numbers)\n")
        arrayA = userInput.split()
        checkA = checkInput(arrayA);
    
    while(not checkB):
        userInput = raw_input("Enter Second Array (Leave Spaces Between Numbers)\n")
        arrayB = userInput.split()
        checkB = checkInput(arrayB)

    sortedArray = merge_Sort(arrayA, arrayB)
    print(sortedArray)
    

if __name__ == '__main__':
    main()
    

