
'''
#1.pascal tringle
n = 5
output:
1
1 1
1 2 1
1 3 3 1 
1 4 6 4 1

#2.Butterfly pattern
n = 4
output:
*     *

#1.pascal triangle
n = int(input())

for i in range(1,n+1):
    num = 1
    for j in range(i):
        print(num,end=" ")
        num = num * (i=j)//(j+i)
    print()
    
'''
n = int(input())
for i in range(1,n+1):
    print("*"*i+" "*(2 *(n-1))+"*"*i)
for j in range(n,0,-1):
    print("*"*j+" "*(2 *(n-j))+"*"*j)   