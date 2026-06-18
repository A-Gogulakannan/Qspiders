"""
15/5/2026

1) wppt fetch the uncomman elements from the both list data type


l1=[1,2,3,4,5]
l2=[6,1,7,2,8]
l3=set(l1).symmetric_difference(l2)
print(list(l3))


2) write a python program to find the all common elements from the both the list data type 

l1=[1,2,3,4,5]
l2=[6,1,7,2,8]
l3=set(l1).intersection(l2)
print(list(l3))

3) Write a python program to find the common elements from the both the list data type without using any builtin method


l1=[1,2,3,4,5]
l2=[6,1,7,2,8]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

or

l=[1,2,3,4]
l2=[]
for i in range(0, len(l)+1):
    l2.append(l[:i])
print(l2)

4) write a python program to add all the even numbers from the first position in the list and add all odd numbers in the last position in the list data type

l1=[1,2,3,4,5,6]
l2=[]
for i in l1:
    if i%2==0:
        l2.insert(0,i)
    else:
        l2.append(i)
print(l2)

or

l=[1,2,3,4,5,6]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
for j in l:
    if j not in l1:
        l1.append(j)
print(l1)

or

l=[1,2,3,4,5,6]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
for j in l: 
    if j%2!=0:
        l1.append(j)
print(l1)


5) Write a python program to find the index position of a target element

n=int(input("Enter number:"))
l1=[2,4,6,8,10,12]
for i in range(len(l1)):
    if l1[i]==n:
        print("The position of the element is",i)
        break
else:
    print("Element not found")


6) Binary search 

arr=[2,4,6,8,10,12]
target=int(input("Enter target:"))
left=0
right=len(arr)-1
found=False
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print("Element found at", mid)
        found=True
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
if not found:
    print("Element not found")

7) Write a python program to count the all non prime numbers in the given list

l=[2,4,5,6,7,8,9,11]
for i in l:
    for j in range(2,i):
        if i%j==0:
            break 
    else:
        l.remove(i)
print(len(l))

8)write a python program to print the costliest product details in the given list variable

l=[[101,5000],[102,6800],[103,7000],[104,9000]]
cost=l[0]
for i in (l):
    if i[1]>cost[1]:
        cost=i
print(cost)

9) Write a python program to check given valid parenthesis or not

s=input("Enter here:")
valid = True
stack=[]
pairs={'(':')','{':'}','[':']'}
for ch in s:
    if ch in pairs:
        stack.append(ch) 
    else:
        if not stack:
            valid=False  
            break  
        if pairs[stack.pop()]!=ch:
            valid=False  
            break
print("Valid parenthesis" if valid and not stack else "Not valid parenthesis")

10) Write a python program to find the missing number in the given list data type

n=[1,3,4,5,7]
n2=n[-1]
for i in range(1,n2+1):
    if i not in n:
        print(i)



"""