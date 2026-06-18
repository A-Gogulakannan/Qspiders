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

"""                                                        25/05/2026                                                        """

'''1) Ip address is valid or not '''

'''
ip=input("Enter ip address:")
valid=True
if len(ip)>=7 and len(ip)<=15:
    if ip.startswith('.') or ip.endswith('.') or '...' in ip:
        valid=False
    else:
        for ch in ip: 
            if not (ch.isdigit() or ch=='.'):
                valid=False  
                break 
    print("Valid" if valid else "Not valid")
else:
    print("Not valid")

4) Write a python program to check middle character in a given odd length of string is a uppercase or not

s='abCde'
if len(s)%2!=0:
    print("Caps" if s[len(s)//2].isupper() else " not caps")
else:
    print("Not odd length")
    
'''