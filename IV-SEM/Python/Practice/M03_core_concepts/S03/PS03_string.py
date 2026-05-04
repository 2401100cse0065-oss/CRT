
'''
#string: collection of characters enclosed '' , " ", ''' ''', """ """
s = "python"
print(s[2])
print(s[1:])

print(s.capitalize())
print(s)

#s[0] = 'P' #strings are immutable
s.replace('p',"P")


#Reverse a string without using built in functions and slice operator

st = input()
res = ""
stop = -1 * (len(st)+1)
for i in range(-1,stop,-1):
    res += st[i]
print(res)                  

def reverse_string(st):
    res = ""
    for ch in st:
        res = ch + res1
    return res1

print(reverse_string("abc"))

def is_palindrome(st):
    st == reverse_string(st)

def frequency_count(s):
    pass
print(frequency_count("abcabc"))

def is_Anagaram(st1,st2):
    pass
print(is_Anagarams("space","paces"))
print(is_Anagarams("abc","abcabc"))
