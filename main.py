
def fibonacci100(n):
    #define function for first 100 numbers
    #name an empty set for numbers
    fibonacci_sequence = []

    #beginning integers
    a = 0
    b = 1


    for x in range(n):
        #in range stops at n-1; need to account for index of 100 somehow
        # or increase range to n=101
        #sequence defined by f1=1 f2=1, and n=(n-1) + (n-2) for n>=3
        fibonacci_sequence.append(a)
        temporary = a
        #temopary variable is IMPORTANT - holds the original value of a
        a = b
        #updates value of a
        b = temporary + b
        #updates value of b

    return fibonacci_sequence
    #moves sequence foward


#generate set of first 100 numbers b/c range is n-1 i went with
# value 101 to be able to have n=100
fibonacci_set = fibonacci100(101)


#print list
print(fibonacci_set)



