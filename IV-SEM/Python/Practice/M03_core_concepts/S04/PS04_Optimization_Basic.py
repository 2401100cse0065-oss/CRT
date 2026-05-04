
def Natural_sum(n):
    if n == 1:
        return 1
    else:
        return n + Natural_sum(n-1) 
    
print(Natural_sum(5))   
print(Natural_sum(10))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(0))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)       
    

def fibanacci(n):
    if n <= 0:
        return "provide a +ve number"
    elif n == 1:
        return 0        
    elif n == 2:
        return 1
    else:
        return fibanacci(n-1) + fibanacci(n-2)
print(fibanacci(1))
print(fibanacci(2))         


#GCD of two numbers
#traditional approach
def gcd(a,b):
    if a < b:
        a,b = b,a
    for i in range(b,0,-1):
        if a % i == 0 and b % i == 0:
            return i    
        
print(gcd(12,15))   
#Euclidean algorithm
def gcd(a,b):   
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(12,15))

    