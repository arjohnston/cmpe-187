import sys

def checkInput(age, gender):
    #check if age and gender inputs are valid
    #if age is not digit or gender is not b/g, warn user
    if(not age.isdigit()):
        print("Invalid Age, Try Again")
        return False
    if(gender.lower() != 'b' and gender.lower() != 'g'):
        print("Invalid Gender, Try Again")
        return False
    return True

def main():
    #takes age and gender input from user
    #compares age and gender to input boundaries to determing ticket type
    #if not eligible, warn user
    inputCheck = False
    while(not inputCheck):
        age = input("How old is the competitor? (In years): ")
        gender = input("What gender is the competitor? (B/G): ")
        inputCheck = checkInput(age, gender)
    age = int(age)

    # Boys and girls age<6,  can participate in Rhyming.
    if(age < 6):
        print("Purchase tickets for the Rhyming Competition")

    # Boys age >7 and <10,  can participate in Storytelling.
    # Girls age >7 and <10,  can participate in Drawing.
    if(age > 7 and age < 10):
        if(gender.lower() == "b"):
            return print("Purchase tickets for the Storytelling Competition")
        if((gender.lower() == "g")):
            return print("Purchase tickets for the Drawing Competition")

    # Boys age >11 and <15,  can participate in a Quiz.
    if(age > 11 and age < 15 and gender.lower() == "b"):
        return print("Purchase tickets for the Quiz Competition")

    # Girls age >10 and <15 ,  can participate in Essay Writing.
    if(age > 10 and age < 15 and gender.lower() == "g"):
        return print("Purchase tickets for the Essay Writing Competition")

    # Girls and boys age >20,  can participate in Poetry.
    if(age > 20):
        return print("Purchase tickets for the Poetry Competition")
    else:
        print("The competitor is not eligible for competition")

# Check for the system version.
# Python 3 is required for the input
# If using python 3, then call the main function
if (sys.version_info > (3, 0)):
    main()
# Otherwise fail gracefully
else:
    print("You need python3 for this")
