def get_positiveinteger():
    #Function to get a valid positive integer from the user
    while True:
        try:
            #continuously prompt the user for input until a valid integer is entered
            numeral = int(input("Enter a positive integer: "))
            #prompt the user to enter a positive integer
            if numeral > 0:
                return numeral
                #Return the valid integer if it is positive
            else:
                print(
                    "The number must be a positive integer. Please try again.")
                #Prompt the user to enter a valid number
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            #deals with non-integer values

def sum_of_divisors(n):
    #function to find the sum of positive divisors of a given number n.
    #if n <= 0:
    #check if the input number is not a positive integer

    total = 0
    #Total sum to zero
    for i in range(1, n + 1):
        #Loop through all integers from 1 to n (inclusive)
        if n % i == 0:
            #Check if i divides n without leaving a remainder
            total += i
            #Add i to the total sum if the condition is met
    return total
    #return the total sum of divisors


#Example
n = get_positiveinteger()
#get a valid positive integer from the user
print(f"Sum of divisors of {n}: {sum_of_divisors(n)}")
#print the sum of divisors