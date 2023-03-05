#q1 Let's write a function falling, which is a "falling" factorial that takes two arguments, n and k, and returns the product of k consecutive numbers, starting from n and working downwards.
def falling(n, k):
    m=1
    for i in range (0,k):
        m=n*m
        n=n-1
    return m

print(falling(4,3))

#q2 Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)
def sum_digits(y):
    a=str(y)
    b=0
    for i in range (0,len(a)):
        b=b+eval(a[i])     
    return b
print(sum_digits(123456789))   

#q3 
def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')
print(ab(10, 20))   


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make
print(bake(0, 29)) 

#q4 Write a function that takes in a number and determines if the digits contain two adjacent 8s.
def double_eights(n):
    a = str(n)
    if a.count('88'):
        return True
    return False
print(double_eights(9098))
