import sys
# User balance to hold available funds
balance = 0

# Function definition to insert money into the balance
# @param amount : Number    amount of money to add to the balance
def insert_money(amount):
    global balance

    # Add the amount entered to the balance
    balance += float(amount)

# Function definition to dispense a Red or Yellow gumball
# @param type : String      Color of gumball to dispense
def dispense_gumball(type):
    global balance

    # Constants for the cost of gumballs
    RED_GUMBALL_COST = 0.05
    YELLOW_GUMBALL_COST = 0.10

    # Select the type of gumball
    # If there is enough balance, subtract the gumball cost
    # and dispense the appropriate gumball
    if (type.lower() == 'red'):
        if(balance >= RED_GUMBALL_COST):
            balance -= RED_GUMBALL_COST
            print("Red gumball has been dispensed")
        else:
            print("Insufficient Balance")

    elif (type.lower() == 'yellow'):
        if(balance >= YELLOW_GUMBALL_COST):
            balance -= YELLOW_GUMBALL_COST
            print("Yellow gumball has been dispensed")
        else:
            print("Insufficient Balance")

    # If it's not a yellow or red gumball, print an erroneous statement
    else:
        print("Unknown gumball type. Try again.")

# Function definition to return the change. Prints the balance
# and resets the balance to 0
def return_change():
    global balance

    print("Returned $" + "%0.2f" % balance)
    balance = 0

# Main function definition. Gets the input and handles the actions:
# Input change: 0.05, 0.10 or 0.25 is accepted and added to the balance
# Select Red or Yellow for gumballs
# Return to return the amount of balance remaining
def main():
    # Continuous while loop until broken
    while(1):
        # Print the current balance, formatted to two decimal places as a standard for currency
        print("\nCurrent balance is: $" + "%0.2f" % balance)

        # Get the user input
        userInput = input(
        "Insert change to increase your balance, retrieve a Red or Yellow gumball or collect your change:\n"
        "\"0.05\": Insert Nickel\n"
        "\"0.10\": Insert Dime\n"
        "\"0.25\": Insert Quarter\n"
        "\"Red\": Receive Red Gumball - $0.05\n"
        "\"Yellow\": Receive Yellow Gumball - $0.10\n"
        "\"Return\": Return Change\n"
        "Input: "
        )

        # If the input is 0.05, 0.10 or 0.25 then insert money
        if (userInput == '0.05' or userInput == '0.10' or userInput == '0.25'):
            insert_money(userInput)

        # If the input is "red" or "yellow", then try to dispense a gumball
        # Convert the string to lowerCase using .lower() to check for all types of input (e.g. "rEd" should equal "red")
        elif (userInput.lower() == 'red' or userInput.lower() == 'yellow'):
            dispense_gumball(userInput)

        # If the input is "Return", then return the balance
        elif (userInput.lower() == 'return'):
            return_change()
            break

        # Otherwise if the input is something other, then print an erroneous message
        else:
            print("Incorrect input, try again.")

# Check for the system version.
# Python 3 is required for the input
# If using python 3, then call the main function
if (sys.version_info > (3, 0)):
    main()
# Otherwise fail gracefully
else:
    print("You need python3 for this")
