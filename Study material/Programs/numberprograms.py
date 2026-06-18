"""
1) Write a python program to check given integer number is a  prime number or not

n=int(input("Enter number:"))
for i in range(2,n):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")

2) Write a python program to find the nth prime number

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

or

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
    prime+=1

3) Write a python program to count number of digits present in the given integer number

n=abs(int(input("Enter number:")))
print(len(str(n)))

4) write a python program to count number of digits present in given integer with out type casting to string

n=abs(int(input("Enter number:")))
count=0
if n==0:
    count+=1
else:
    while n>0:
        n//=10
        count+=1
print(count)


5) write a python program to check given integer number is a palindrome or not

n=abs(int(input("Enter number:")))
if str(n)==(str(n)[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")

6) Write a python program to print only even numbers from the given integer

n=abs(int(input("Enter number:")))
while n!=0:
    rem=n%10
    if rem%2==0:
        print(rem)
    n//=10

7)Write a python program to print all odd digits from the given integer Number

n=abs(int(input("Enter number:")))
while n!=0:
    rem=n%10
    if rem%2!=0:
        print(rem)
    n//=10

8) Write a python program to reverse the given integer number

n=abs(int(input("Enter number:")))
print(int(str(n)[::-1]))

9) Write a python program to reverse the given integer number without using type casting

n=abs(int(input("Enter number:")))
digit=0
while n!=0:
    rem=n%10
    digit=digit*10+rem
    n//=10
print(*l)

10)Write a python program to check the given integer number is a spy number or not

n=abs(int(input("Enter number:")))
sum=0
prod=1
for i in str(n):
    sum+=int(i)
    prod*=int(i)
print("Spy number" if sum==prod else "Not a spy number")#spy number is product of individual digits is equal to addition of individual digits

11)Write a python program to check the given integer number is a neon number or not

n=int(input("Enter number:"))
sum=0
s=n*n
for i in str(s):
    sum+=int(i)
print("Neon number" if sum==n else "Not a neon number")#Neon number means addition of individual digits of the square of the number is eqaul to that number

12)Write a python program to check the given integer number is a amstrong number or not

n=int(input("Enter number:"))
sum=0 
l=len(str(n))
for i in (str(n)):
    sum+=(int(i)**l)
print("Armstrong number" if sum==n else "Not a Armstrong number")

13)Write a python program to check given integer number is a strong number or not

n=int(input("Enter number:"))
sum=0
for i in (str(n)):
    fact=1
    for j in range(1,int(i)+1):
        fact=fact*j
    sum+=fact
print("strong number" if sum==n else "Not a strong number")

14) Write a python program to convert the integer number to binary number

n=int(input("Enter number:")) 
b=bin(n)
print(int(b[2::]))

15) Write a python program to convert integer number to binary number without using bin function

n=int(input("Enter number"))
digit=''
while n>0:
    rem=n%2
    digit=str(rem)+digit
    n=n//2
print(int(digit))

16) write a python program to convert integer number to binary number without using bin function and with out taking empty string

n=int(input("Enter number"))
binary=[]
while n>0:
    rem=n%2
    binary.insert(0,rem)
    n//=2
print(*binary,sep='')

"""