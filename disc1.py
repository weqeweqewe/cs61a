'''
#1
def wears_jacket(temp, raining):
    return  temp<=60 or  raining ==True
print(wears_jacket(90, False))

'''
#2
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

print(square(so_slow(5)))
无穷大

#3
def is_prime(n):
     c=0
     for i in range(1,n+1):
       
        if n%i==0:
            c=c+1
        elif c<=2:
            return True 
        else:
            return False
print(is_prime(18))



            

