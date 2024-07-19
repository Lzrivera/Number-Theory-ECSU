class PollardsPminus1:
    def __init__(self, number):
        #initialize with the number to factor
        self.number = number

    def gcd(sewlf, a, b):
        # define fuction for greatest common divisor of two
        # positive integers, not both zero
        # implement the Euclidean Algorithm [gcd(a,b) = gcd(a,b-a) when a, b are integers]
        while b != 0:
            # loop to check that b is not equal to zero
            d = b
            # d stores the current value of b
            b = a % b
            # this computes the remainder when a is divided by b and stored in b variable
            a = d
            # this asignes the value of d, the old b, to variable a

        return a
        # this will be the gcd of the inputted integers

    def factor(self):
        #factor the number using Pollards p-1 method
        n = self.number
        if n<= 1:
            return None
            #return invlaid input
        a = 2
        #intialize a to 2
        for j in range(2, n):
            #loop form 2 to n-1
            a = pow(a, j, n)
            #calculate a^j % n
            d = self.gcd(a - 1, n)
            #calculate gcd(a-1, n) using eludian gdc fnx
            if 1 < d < n:
                return d
                #if a non-trivial factor is found, return it
        return None
        #if no factor is found, return none

