#q1 Write a function that takes in a function cond and a number n and prints numbers from 1 to n where calling cond on that number returns True

def keep_ints(cond, n):
    i=1
    cond=is_even
    while i<n+1:
        if cond(i)==True:
            print( i)
        i=i+1
        
def is_even(x):
    return x % 2 == 0

print(keep_ints(is_even, 6))

#2
def keep_ints(n):
    def h(func):
        i=1
        func=is_even
        while i<n+1:
            if func(i)==True:
                print( i)
            i=i+1
    return h   

def is_even(x):
    return x % 2 == 0

print(keep_ints(6)(is_even))

#3
def print_n(n):
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print


