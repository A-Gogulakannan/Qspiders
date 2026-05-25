"""15/5/2026"""

"""1) wppt fetch the uncomman elements from the both list data type"""

"""
l1=[1,2,3,4,5]
l2=[6,1,7,2,8]
l3=set(l1).symmetric_difference(l2)
print(list(l3))
"""

"""2) write a python program to find the all common elements from the both the list data type """

"""
l1=[1,2,3,4,5]
l2=[6,1,7,2,8]
l3=set(l1).intersection(l2)
print(list(l3))
"""

"""3) Write a python program to find the common elements from the both the list data type without using any builtin method"""

"""
l1=[1,2,3,4,5]
l2=[6,1,7,2,8]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)
"""


"""
l=[1,2,3,4]
l2=[]
for i in range(0, len(l)+1):
    l2.append(l[:i])
print(l2)
"""

"""4) write a python program to add all the even numbers from the first position in the list and add all odd numbers in the last position in the list data type"""

"""
l1=[1,2,3,4,5,6]
l2=[]
for i in l1:
    if i%2==0:
        l2.insert(0,i)
    else:
        l2.append(i)
print(l2)
"""

"""
l=[1,2,3,4,5,6]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
for j in l:
    if j not in l1:
        l1.append(j)
print(l1)
"""

"""
l=[1,2,3,4,5,6]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
for j in l: 
    if j%2!=0:
        l1.append(j)
print(l1)
"""


"""                                                        16/05/2026                                                       """


"""                                                        18/05/2026                                                       """


"""                                                       ""NUMBERS""                                                       """


"""1) Write a python program to check given integer number is a  prime number or not"""

"""
n=int(input("Enter number:"))
for i in range(2,n):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")
"""

"""2) Write a python program to find the nth prime number """

"""
n=int(input("Enter number:"))
count=0
prime=1
while count<n:
    prime+=1
    for i in range(2,prime):
        if prime%i==0:
            break
    else:
        count+=1
print(prime)
"""

"""
n=int(input("Enter number:"))
prime=2
prime_count=0
while prime_count<=n:
    rem_count=2
    for i in range(2,prime):
        if prime%i==0:
            rem_count+=1
            break
    if rem_count==2:
        prime_count+=1
        if prime_count==n:
            print(prime)
            break
    prime+=1"""

"""3) Write a python program to count number of digits present in the given integer number"""

"""
n=abs(int(input("Enter number:")))
print(len(str(n)))
"""

"""4) write a python program to count number of digits present in given integer with out type casting to string"""

"""
n=abs(int(input("Enter number:")))
count=0
if n==0:
    count+=1
else:
    while n>0:
        n//=10
        count+=1
print(count)
"""

"""5) write a python program to check given integer number is a palindrome or not"""

"""
n=abs(int(input("Enter number:")))
if str(n)==(str(n)[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")
"""


"""                                                        19/05/26                                                        """


"""1) Write a python program to print only even numbers from the given integer"""

"""
n=abs(int(input("Enter number:")))
while n!=0:
    rem=n%10
    if rem%2==0:
        print(rem)
    n//=10
"""

"""2)Write a python program to print all odd digits from the given integer number"""

"""
n=abs(int(input("Enter number:")))
while n!=0:
    rem=n%10
    if rem%2!=0:
        print(rem)
    n//=10
"""

"""3) Write a python program to reverse the given integer number"""

"""
n=abs(int(input("Enter number:")))
print(int(str(n)[::-1]))
"""

"""4) Write a python program to reverse the given integer number without using type casting"""

"""
n=abs(int(input("Enter number:")))
digit=0
while n!=0:
    rem=n%10
    digit=digit*10+rem
    n//=10
print(*l)
"""


"""                                                        20/05/2026                                                        """


"""1)Write a python program to check the given integer number is a spy number or not"""

"""
n=abs(int(input("Enter number:")))
sum=0
prod=1
for i in str(n):
    sum+=int(i)
    prod*=int(i)
print("Spy number" if sum==prod else "Not a spy number")#spy number is product of individual digits is equal to addition of individual digits
"""

"""2)Write a python program to check the given integer number is a neon number or not """

"""
n=int(input("Enter number:"))
sum=0
s=n*n
for i in str(s):
    sum+=int(i)
print("Neon number" if sum==n else "Not a neon number")#Neon number means addition of individual digits of the square of the number is eqaul to that number
"""

"""3)Write a python program to check the given integer number is a amstrong number or not"""

"""
n=int(input("Enter number:"))
sum=0 
l=len(str(n))
for i in (str(n)):
    sum+=(int(i)**l)
print("Armstrong number" if sum==n else "Not a Armstrong number")
"""

"""4)Write a python program to check given integer number is a strong number or not"""

"""
n=int(input("Enter number:"))
sum=0
for i in (str(n)):
    fact=1
    for j in range(1,int(i)+1):
        fact=fact*j
    sum+=fact
print("strong number" if sum==n else "Not a strong number")
"""

"""                                                        21/05/2026                                                        """

"""1) Write a python program to find the index position of a target element"""

"""
n=int(input("Enter number:"))
l1=[2,4,6,8,10,12]
for i in range(len(l1)):
    if l1[i]==n:
        print("The position of the element is",i)
        break
else:
    print("Element not found")
"""

"""2) Binary search """

"""
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
"""

"""3) Write a python program to convert the integer number to binary number"""

"""
n=int(input("Enter number:")) 
b=bin(n)
print(int(b[2::]))
"""

"""4) Write a python program to convert integer number to binary number without using bin function"""

"""
n=int(input("Enter number"))
digit=''
while n>0:
    rem=n%2
    digit=str(rem)+digit
    n=n//2
print(int(digit))
"""

"""5) write a python program to convert integer number to binary number without using bin function and with out taking empty string"""

"""
n=int(input("Enter number"))
binary=[]
while n>0:
    rem=n%2
    binary.insert(0,rem)
    n//=2
print(*binary,sep='')
"""

"""                                                        22/05/2026                                                        """

"""1) Write a python program to reverse a given string"""

"""
n=input("Enter string:")
print(n[::-1])
"""

"""2) Write a python program to reverse the string without slicing"""

"""
s="input"
a=''
for i in s:
    a=i+a
print(a)
"""

"""3) Write a python program to check given string is palindrome"""

"""
s=input("Enter string:")
print("Palindrome" if s==(s[::-1]) else "Not")
"""

"""4) Write a python program to check given string is palindrome without using slicing"""

"""
s=input("Enter string:")
a=''
for i in s:
    a=i+a
print("Palindrome" if s==a else "Not")
"""

"""
SPLIT BUILTIN METHOD:

    ->Split is a string built in method which is used to split the given string based on the given seperator
    ->SYNTAX:
    ->The default separator of the split built in function is space
    ->The default value of the max split is -1, which means there is no limit for spliting
"""

"""5) Write a python program to count the words in a string"""

"""
s=input("Enter string:")
print(len(s.split()))
"""

"""
s=input("Enter string:")
a=s.split()
count=0
for i in a:
    count+=1
print(count)
"""

"""6) Write a python program to count the number of words in the given string with out using split builtin method"""

"""
s = input("Enter string: ")
s = s.strip()

if len(s) != 0:
    count = 1
    for i in s:
        if i == ' ':
            count += 1
    print(count)
else:
    print(0)
"""

"""                                                      ASSIGNMENT                                                         """

"""1) write a python program to count the number of words in the given string with out using split builtin method and strip builtin method """

"""
s="Write a python program to count   the words in a string   "
l=[]
s=s+" "
a=''
for i in s:
    if i!=' ':
        a=a+i
    elif a!='':
        l.append(a)
        a=''
print(len(l))
"""

"""2) Write a python program to find the duplicate characters in given string"""

"""
s="abcdaafs  bcdfg"
duplicate=[]
seen=[]
for i in s:
    if i!=' ':
        if i in seen:
            if i not in duplicate:
                duplicate.append(i)
        else:
            seen.append(i)
print(*duplicate,sep='')
"""

"""3) Write a python program to remove duplicate characters in given string"""

"""#if we want to remove the letter that is getting repeated completely
s='aabbccddafg'
org=''
for i in s:
    if i!=' ':
        if s.count(i)==1:
            org+=i
print(org)
"""

"""#if we want to remove only repeated character
s='aabbccddafg'
org=''
duplicate=[]
for i in s:
    if i!=' ': #if we want to include space then remove this
        if i not in duplicate:
            org=org+i
            duplicate.append(i)
print(org)
"""

"""4) Write a python program to check given string is anagram"""

"""
s='listen'
s1='silent'
if sorted(s)==sorted(s1):
    print("Anagram")
else:
    print("Not anagram")
"""

"""WITHOUT SORTED"""
"""
s='listen'
s1='silent'
anagram=True
if len(s)!=len(s1):
    anagram=False
else:
    for i in s:
        if s.count(i)!=s1.count(i):
            anagram=False 
            break
            
print("Anagram" if anagram==True else "Not anagram")
"""

"""5) Write a python program to find frequency of characters in the given string"""

"""
s="aaabbbcccdddaaabbbcccefgh"
d={}
for i in s:
    d[i]=s.count(i)  
print(d.items())
"""

"""WITHOUT COUNT"""

"""
s="aaabbbcccdddaaabbbcccefgh"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(*d.items())
"""

"""6) Write a python program to convert characters to upper case for given string without using string builtin Functions"""

"""
s='abcd  Ghj'
a=''
for i in s:
    if i!=' ':
        if ord(i)>96 and ord(i)<123:
            b=ord(i)-32
            a=a+chr(b)
        else:
            a+=i 
    else:
        a=a+i  
print(a)
"""

"""7) Write a python program to convert string to lower case without string built in function"""

"""
s='AbCd  Ghj '
a=''
for i in s:
    if i!=' ':
        if ord(i)>64 and ord(i)<91:
            b=ord(i)+32
            a=a+chr(b)
        else:
            a+=i 
    else:
        a=a+i  
print(a)
"""

"""8) Write a python program to toggle each character(a->A,B->b)"""

"""
s='aBcD eFgH'
print(s.swapcase())
"""

""" WITH OUT STRING BUILTIN FUNCTIONS """

"""
s='AbCd  Ghj '
a=''
for i in s:
    if i!=' ':
        if ord(i)>64 and ord(i)<91:
            b=ord(i)+32
            a=a+chr(b)
        elif ord(i)>96 and ord(i)<123:
            b=ord(i)-32
            a=a+chr(b)
        else:
            a+=i 
    else:
        a=a+i  
print(a)
"""

"""9) Write a python program to count alphabets, digits and special characters"""

"""
s='abcD @145Cd  '
d={}
seen=[]
for i in s:
    if i not in seen:
        d[i]=s.count(i)
        seen.append(i)
print(d)
"""

""" WITHOUT COUNT"""

"""
s='abcD @145Cd  '
d={}
for i in s:
    if i not in d:
        d[i]=1  
    else:
        d[i]+=1
print(d)
"""


""" Test"""
"""
n=[5,1,3,2,6]
a=len(n)  
for i in range(a):
    for j in range(i+1,a):
        if(n[i]>n[j]):
            n[i],n[j]=n[j],n[i]
print(n[0])
print(n[a-1])
"""

"""
n=[5,1,3,2,6]
n.sort()
print(n[len(n)-2])
"""

"""
n=[5,1,3,2,6]
n.sort()
print(n[1])
"""

"""
s='ac  cadef'
seen=[]
duplicate=[]
for i in s:
    if i!=' ':
        if i not in seen:
            seen.append(i)
        else:
            duplicate.append(i)   
for i in seen:
    if i not in duplicate:
        print(i) 
        break
"""
"""
s='ac  cadef'
seen=[]
duplicate=[]
for i in s:
    if i!=' ':
        if i not in seen:
            seen.append(i)
        else:
            duplicate.append(i)
print(duplicate[0])
"""
'''
s = "Bitty bought a butter and the butter was bitter,so she decided to change the butter so that it would taste better"
d = ""
for i in s:
    if i != " ":
        d = d + i
print(len(d))
sr = len(d) ** 0.5
print("Square root:", sr)
s1 = d[0 : (round(sr))]
print(s1)
print()
i = 0
j = round(sr)
for k in range(round(sr)):
    z=''
    z=d[i:j]
    if len(z)==(round(sr)):
        print(z)
    i += round(sr)
    j += round(sr) 
'''

'''
s = "Bitty bought a butter and the butter was bitter,so she decided to change the butter so that it would taste better"
s1=s.replace(' ','')
le=int(len(s1)**0.5)
for i in range(0,len(s1),le):
    print(s1[i:i+le])
'''