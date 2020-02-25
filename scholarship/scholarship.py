import sys

# todo: check for invalid input (e.g. negative values)

# Get an input response of 'Y/y' or 'N/n'
def get_boolean_input(message):
    response = input(message)

    # Check to see if the response is in the correct format
    while (response.lower() != 'y' and response.lower() != 'n'):
        print("Invalid input, try again.")
        response = input(message)

    # return the response once Y/y or N/n
    return response

# Get the eligibility of a scholarship
def main():
    # Get age input
    # Check if in the age 18 - 24
    # If not, then return "not eligible"
    userInput = int(input("How old are you? (in years): "))

    # A. Student is between the  age 18 and 24 (boundary value included)
    if (userInput < 18 or userInput > 24):
        print(0)
        return

    # Get number of years lived in CA input
    # if >= 2 years, continue
    # else
    # boolean input: have the parents paid CA state tax for at least 1 year?
    # if no, then return "not eligible", otherwise continue
    userInput = int(input("How many years have you lived in California? "))

    # B. Student has lived in California for last 2 years, if he fails this criterion, check if satisfies D.
    # D. Parents of the student have paid California state tax for at least 1 year in their lifetime.
    if (userInput < 2):
        # userInput = input("Have your parents paid California state tax for at least 1 year in their lifetime? (Y/N): ")
        userInput = get_boolean_input("Have your parents paid California state tax for at least 1 year in their lifetime? (Y/N): ")

        if (userInput.lower() != 'y'):
            print(0)
            return

    # Boolean input: Have you worked part time for at least 6 months in a relevent field of study?
    # yes: continue
    # no: have you volunteered for a cause and have valid proof? Yes, continue. No, return "not eligible"
    # OR:  Do you have a household income less than 5000$ per annum?
    userInput = get_boolean_input("Have you worked part time for at least 6 months in a relevent field of study? (Y/N): ")

    # C. Has worked part time for at least for 6 months in the relevant field of study, if he fails this criterion, check if satisfies E.
    if (userInput.lower() != 'y'):
        userInput = get_boolean_input("Have you volunteered for a cause and have valid proof of it? (Y/N): ")

        # E. Has volunteered for a cause and has a valid proof of it.
        if (userInput.lower() != 'y'):
            userInput = get_boolean_input("Does your household have income less than 5000$ per annum? (Y/N): ")

            # F. Has household income less than 5000$ per annum then one need not satisfy criteria C, he will be redirected to "Dean for consideration"
            if (userInput.lower() == 'y'):
                print("Dean for consideration")
                return

    # If all passes, you are eligible
    print(1)

# Check for the system version.
# Python 3 is required for the input
# If using python 3, then call the main function
if (sys.version_info > (3, 0)):
    main()
# Otherwise fail gracefully
else:
    print("You need python3 for this")
