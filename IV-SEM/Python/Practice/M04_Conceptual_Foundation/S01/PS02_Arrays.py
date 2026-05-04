
#input : [12,45,36,78,96]
#output : [96 78 36 45 12]
#traditional 
li = [12,45,36,78,96]
res = []
stop = -1 * (len(li)+1)
for i in range(-1,stop,-1):
    res.append(li[i])
print(res)
#list compreshension
res1 = [li[i] for i in range(-1,stop,-1)]
print(res1)

#using swapping technique
li = [12,45,36,78,96]
n = len(li)
print("before swapping",li)
for i in range(n//2):
    li[i],li[n-1-i] = li[n-1-i],li[i]
print("after swapping",li)

li = [12,45,36,78,96]
res = []
for ele in li:
    res.insert(0,ele)
print(res)

#check if an arrasy is sorted
# input : [12,23,45,56,69,100] ==> output : True
# output : [12,45,36,78,96] ==> output : False
def check_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

#Count Frequency of Elements
#input : [1,2,3,4,1,2,5,2,4]
#output : [1:2, 2:3, 3:1, 4:2, 5:1]
li = [1,2,3,4,1,2,5,2,4]
res = {}
for ele in li:
    if ele  not in res:
        res[ele] = 1
        