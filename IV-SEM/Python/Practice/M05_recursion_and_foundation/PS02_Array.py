
def Array_sum(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i]
    return s                    
print(Array_sum([1,2,3,4,5]))       

#Recursion approach
def Array_sum(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + Array_sum(nums[1:])
    
print(Array_sum([1,2,3,4,5]))   

#Recusive Approach-2
de0f Array_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + Array_sum(nums[1:])   


#Reverse an array
def Reverse_array(nums,i,j):
    if i >= j:
        return
    else:
        nums[i],nums[j] = nums[j],nums[i]
        Reverse_array(nums,i+1,j-1)     

print(Reverse_array([1,2,3,4,5],0,4))

#Reverse a string
def Reverse_string(st):
    if len(st) == 0:
        return ""
    else:
        return st[-1] + Reverse_string(st[:-1])

print(Reverse_string("acd"))

def is_palindrome(st):
    return st == Reverse_string(st)

print(is_palindrome("abc"))
print(is_palindrome("abcba"))


#Digital root sum 
#386 ==> 3+8+6 == 17 == 1+7 == 8
def Digital_root_sum(n):      
    if n <=  9:
        return n
    s = sum([int(ch) for ch in str(n)])
    return Digital_sum(s)

print(Digital_root_sum(386))    
