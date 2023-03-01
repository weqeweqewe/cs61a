#q2 A Plus Abs B  : Fill in the blanks in the following function for adding a to the absolute value of b, without calling abs. You may not modify any of the provided code other than the two blanks.
def a_plus_abs_b(a, b):
    if b < 0:
        f = a-b
    else:
        f = a+b
    return f(a, b)


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = a-b
    else:
        f = a=b
    return f(a, b)

#q3 Two of Three :Write a function that takes three positive numbers as arguments and returns the sum of the squares of the two smallest numbers. Use only a single line for the body of the function.
def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return  x*x+y*y+z*z-max(x,y,z)**2

#q4 Largest Factor: Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
#第一种解法
b=[]
a=eval(input('请输入一个数字：'))    #'int' object is not iterable  ：int’对象不可迭代
for i in range (1,a):
    if a %i==0:
        b.append(i)
c=max(b)
print(c)
#官方solution
def largest_factor(n):
    factor = n - 1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1
print(largest_factor(15))

#q5 If Function vs Statement :Let's try to write a function that does the same thing as an if statement.
def if_function():
不会 看不懂





#q6 Hailstone 
def hailstone(n):
    c=1
    while n !=1:
        if n%2 == 0:
            n=n/2
        else:
            n=3*n+1
        c=c+1
    print(c)
print(hailstone(10))
#官方solution
def hailstone(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2      # Integer division prevents "1.0" output
        else:
            n = 3 * n + 1
        length = length + 1
    return length
print(hailstone(10))
