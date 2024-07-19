from gcd import PollardsPminus1


def get_positiveinteger():
    # Define a function to get a valid positive integer from the user
    while True:
        try:
            # Continuously prompt the user for input until a valid integer is entered
            numeral = int(input("Enter a positive integer between 2 and 6 million: "))
            if 2 <= numeral <= 6000000:
                # Check if integer is between 2 and 6 million
                return numeral
                # Return the valid integer
            else:
                print("The number must be between 2 and 6 million. Please try again.")
                # Prompt the user to enter a valid number if the condition is not met
        except ValueError:
            print("Invalid. Please enter a positive integer.")
            #deals with non-integer values

def main():
    #define the main fnx
    number = get_positiveinteger()
    #get a valid positive integer from the user
    pollards = PollardsPminus1(number)
    #create an instance of Pollards p-1 with the input number
    factor = pollards.factor()
    #factor the input numeral using Pollards p-1 method
    if factor:
        print(f"A non-trivial factor of {number} is: {factor}")
        #print the factor if foudn
    else:
        print(f"No non-trivial factor found for {number} using Pollard's p-1 method.")
        #print message if no factor is found

if __name__ == '__main__':
    main()
    #call the main fnx directly

