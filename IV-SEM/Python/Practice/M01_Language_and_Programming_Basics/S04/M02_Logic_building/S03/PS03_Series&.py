 '''
 Arithmetic series:
 input : 1 2 
 output : 1 3 5 7 9 11 13 15 17 19
 '''

 a = int(input())
 d = int(input())
 for i in range(10):
    print(a + i * d ,end= " ")
'''
a = int(input())
r = int(input())
for i in range(10):
    print(a*(r ** i) ,end=" ")

Fibanocci series:
n = 5
0 1 1 2 3 
'''
n = int(input())
a = 0 
b = 1
for i in range(n):
    print(a, end= " ")
    a,b = b,a+b

print()

li = [0,1]
for i in range(2,n):
    li.append(li[i-2]+ li[i-1])
print(li)
