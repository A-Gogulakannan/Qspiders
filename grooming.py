#27/05/2026 HTC

#Given ip address is valid or not

'''
s=input("Enter string:")
valid=True
if len(s)>=7 and  len(s)<=15:
    if s[0]=='.' or s[-1]=='.' or '...' in s:
        valid=False
    else:
        for ch in s:
            if not (ch.isdigit() or ch=='.'):
                valid=False
                break
    print("Valid" if valid else "Invaid")
else:
    print("Invalid")
'''

#costliest

'''
l=[[101,1000],[102,5000],[103,4000],[104,2000]]
costliest=l[0]
for i in l:
    if i[1]>costliest[1]:
        costliest=i  
print(costliest)
'''

#non-prime numbers

'''
l=[1,2,3,4,5,6,7,8,9]
count=0  
for i in l:
    for j in range(2,i):
        if i%j==0:
            count+=1
            break
print(count)
'''

#clean the string "Madam@123 @Madam"

'''
s="Madam@123 @Madam"
res=""
for i in s:
    if i.isalnum():
        res+=i
print(res)
'''

#frequency of characters

'''
s="Madam@123 @Madam"
from collections import Counter
d=Counter(s)
print(dict(d))
'''
'''
s="Madam@123 @Madam"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
'''

