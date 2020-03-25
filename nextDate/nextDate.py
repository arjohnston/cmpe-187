import sys
import datetime

# get input func
def get_input(message):
    dateIsValid = False
    dateFormat = "%m/%d/%Y"

    # while loop false until valid date entered
    # check to ensure the year is within the range 1900-2099
    while (not dateIsValid):
        userInput = input(message)

        # try parsing the date from the input. If invalid, then it fails & is caught by the
        # except block
        try:
            date = datetime.datetime.strptime(userInput, dateFormat)

            # ensure the YYYY is in the range of 1900 - 2099 inclusively
            if (date.date().year < 1900 or date.date().year > 2099):
                print("Invalid year. Please enter a year between 1900 and 2099 inclusively.")

            # if all is valid, then break the while loop & return the value
            else:
                dateIsValid = True
        except:
            print("Invalid input, try again.\n")

    # return date
    return date

# get next date func
def get_next_date(date):
    # Get the next date
    nextDate = date + datetime.timedelta(days=1)

    # Convert the string to MM/DD/YYYY format
    nextDateString = str(nextDate.date().month) + '/' + str(nextDate.date().day) + '/' + str(nextDate.date().year)

    # Return the string
    return nextDateString

# Main
def main():
    # get date MM/DD/YYYY between 1900-2099
    dateInput = get_input("Enter a date in the format MM/DD/YYYY: ")

    # get next date
    nextDate = get_next_date(dateInput)

    # print the next date
    print(nextDate)

# Check for the system version.
# Python 3 is required for the input
# If using python 3, then call the main function
if (sys.version_info > (3, 0)):
    main()
# Otherwise fail gracefully
else:
    print("You need python3 for this")
