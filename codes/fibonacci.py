import datetime
'''
We are given that the fibonacci can be expressed as a simple formula as
fn = fn-1 + fn-2
and the initial values given being 
f0 = 0
f1 = 1
'''
# simple program
input_given = int(input(""))


def fibonacci(n):
    if(n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


start = datetime.datetime.now()
print(fibonacci(input_given))
print(datetime.datetime.now()-start)

# with storing values
'''
Here we are going through a linear list and just storing all the fibonacci numbers 
and just returning the nth number
'''


def fibonacci_with_values(n):

    values = [0, 1]
    for x in range(2, n+1):
        # print(x, n, n-1, n-2)
        values.append(values[x-1]+values[x-2])

    return values[n]


start = datetime.datetime.now()
print(fibonacci_with_values(input_given))
print(datetime.datetime.now()-start)

# note that we have to store entire list in the above method but we only need the previous 2 for finding the nth fibonacci number


def fibonacci_space_optimised(n):
    # setting the defaults
    a = 0
    b = 1
    if(n == 0):
        return a
    elif(n == 1):
        return b
    else:
        for x in range(2, n+1):
            c = a+b
            a = b
            b = c
        return c


start = datetime.datetime.now()
print(fibonacci_space_optimised(input_given))
print(datetime.datetime.now()-start)