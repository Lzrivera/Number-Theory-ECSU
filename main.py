
def gcd(a, b):
    #define fuction for greatest common divisor of two
    #positive integers, not both zero
    #implement the Euclidean Algorithm [gcd(a,b) = gcd(a,b-a) when a, b are integers]
    while b != 0:
        #loop to check that b is not equal to zero
        d = b
        #d stores the current value of b
        b = a % b
        #this computes the remainder when a is divided by b and stored in b variable
        a = d
        #this asignes the value of d, the old b, to variable a


    return a
    #this will be the gcd of the iputed integers

#input integer values
integer1 =  int(input("Enter the first positive integer:"))
integer2 =  int(input("Enter the second positive integer:"))


#Find result by calling the function with inputted values
result = gcd(integer1, integer2)

#print the GCD and intergers used
print(f"the GCD of {integer1} and {integer2} in: {result}")


