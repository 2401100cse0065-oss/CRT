
#GCD of two numbers
a = int(input())
b = int(input())    
min_num = min(a,b)

for i in range(1,min_num+1):

    if a%i == 0 and b%i == 0:
        gcd = i     
print(gcd)

#solution 2
while b != 0:
    a, b = b, a % b     
print(a)

#LCM
a = int(input())
b = int(input())    
import math
lcm = (a * b) // math.gcd(a, b)
print(lcm)
'''

def check_perfect_number(n):
    s = 0
    for i in range(1,n//2 + 1):
        if n % i == 0:
            s += i
            "perfect number" if s == n else "not perfect"

            

























