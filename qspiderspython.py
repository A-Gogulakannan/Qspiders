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
'''

'''2) Write a python program to count the all non prime numbers in the given list'''

'''
l=[2,4,5,6,7,8,9,11]
for i in l:
    for j in range(2,i):
        if i%j==0:
            break 
    else:
        l.remove(i)
print(len(l))
'''

'''3) write a python program to print the costliest product details in the given list variable '''

'''
l=[[101,5000],[102,6800],[103,7000],[104,9000]]
cost=l[0]
for i in (l):
    if i[1]>cost[1]:
        cost=i
print(cost)
'''

'''4) Write a python program to check middle character in a given odd length of string is a uppercase or not'''

'''
s='abCde'
if len(s)%2!=0:
    print("Caps" if s[len(s)//2].isupper() else " not caps")
else:
    print("Not odd length")
'''

"""                                                        26/05/2026                                                        """

'''1) Write a python program to check given valid parenthesis or not'''

'''
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

'''

'''2) Write a python program to find the missing number in the given list data type'''

'''
n=[1,3,4,5,7]
n2=n[-1]
for i in range(1,n2+1):
    if i not in n:
        print(i)
'''

'''3) Write a python program to '''
'''n=4
for i in range(n):
    for j in range(n):
        if i==n-1 or i+j==n-1 :
            print("*", end='')
        else: 
            print(" ",end='')
print()'''


''' Patterns'''

'''
def hallow_pyramid(n):
    for i in range(n):
        for j in range(n):
            if i+j==(n//2) or i-j==(n//2) or i+j==((3 * n // 2) - 1) or j-i ==(n//2):
                print('*', end=" ")
            else:
                print(" ",end=" ")
        print()
def right_hallow_triangle(n):
    for i in range(n):
        for j in range(n):
            if j==0 or (i <= n//2 and j == 2*i) or (i > n//2 and j == 2*(n-i-1)):
                print('*', end=" ")
            else:
                print(" ",end=" ")
        print()
def top_hallow_triangle(n):
    for i in range(n):
        for j in range(n):
            if i==(n-1) or (i%2==0 and (j==(n//2 - i//2) or j==(n//2 + i//2))):
                print('*', end=" ")
            else:
                print(" ",end=" ")
        print()

n=int(input("Enter rows:"))
hallow_pyramid(n)
right_hallow_triangle(n)
top_hallow_triangle(n)

'''


"""                                                        27/05/2026                                                        """

'''

->Functions:

    ->Function is a block of code used to do a specific task.
    ->To work on the function it should have 3 main parts.
        ->Function definition or declaration.
        ->Function body.
        ->Function calling.
    ->SYNTAX:
        def function_name(parameters):
            #statements
        function_name(arguments)

->Advantages of functions:

    ->REUSABILITY:

        ->It means declare the function ones and reuse many times.

    ->MODULARITY:

        ->It means divide the bigger task into smaller parts, complete the smaller task to achive the bigger task.
    
    ->NOTE: Rules on working with the function:

            ->Function key word should start with def keyword.
            ->Function parameters are optional.
            ->Function calling should be always after the function declaration or definition.
            ->Ones the function is declared, we can call that in any file with the help of packages and modules.

    ->TO CREATE AN FUNCTION IN PYTHON:

        ""def sam():
              print("HI")
          sam()#first time calling
          sam()#second time calling

    ->TYPES OF FUNCTIONS IN PYTHON:

        ->Builtin functions
        ->User defined or custom function.
        ->Nested function.
        ->Miscellaneous function.
        ->Lamda or anonymous function

        ->BUILTIN FUNCTION.

            ->Functions which are already present in python or which is already developed by the developers, we can use those functions in our programming life whenever we required but we cannot change the meaning of those functions.
            ->EXAMPLE: print(),sum(),ord(),chr(),...
            ->NOTE: In python many builtin functions are there.

        ->USER DEFINED FUNCTION OR CUSTOM FUNCTION.

            ->The function which is designed by the programmers based on the user requirement or project requirement
            ->EXAMPLE:
                ""def sqr(n1,n2):
                    print(n1*n2)
                  sqr(10,20)
                  sqr(5,6)""

                  OUTPUT: 200
                          30

        NOTE:PARAMETERS: Parameters are the names passing to the function during the function declaration or function definition.
        NOTE:ARGUMENTS: Arguments are the values passing to the parameters during the function call.
        NOTE:Number of parameters declared during the function declaration, for all the parameters need to pass the values.
        NOTE:If we miss a single value also, python will throws a error.

        ->RETURN KEYWORD:

            ->It is a function keyword in python which is used to return any type of value from the function.
            ->Return keyword can be only used inside the function or method.
            ->Return keyword will send the output to the function call.

            ->SYNTAX:
                def function_name(params):
                    ----------
                    ----------
                    return any_data

            ->EXAMPLE:
                ""def addition(n1,n2):
                    return n1+n2
                  var=addition(10,20)
                  print(var)""

                OUTPUT: 30

        ->Write a python program to create a function and it should accept a parameter and return a msg wheather the given is even or odd

            def even_odd(n):
                    return 'even' if n%2==0 else 'odd'
            print(even_odd(5))


        ->TYPES OF USER-DEFINED FUNCTIONS:

            ->Function without parameter and without return type:
                    
                def addition():
                    n1=int(input())
                    n2=int(input())
                    print(n1+n2)
                addition()

            ->Function with parameter and without return type:

                def addition(n1.n2):
                    print(n1+n2)
                addition(10,20)

            ->Function without parameter and with return type:

                def addition():
                    n1=int(input())
                    n2=int(input())
                    return n1+n2
                addition()

            ->Function with parameter and with return type:

                def addition(n1,n2):
                    return n1+n2
                addition(10,20)

            ->Function with recursion or without recursion:


        ->NESTED FUNCTIONS:

            ->It is a function which is declared inside the scope of another function is called nested function.
            ->If any function is declared inside another function then it becomes a local function inside another function.
            ->A inner function can be called only inside the scope of outer function.
            ->EXAMPLE:
                def outer():
                    print("I am outer function")
                    def inner1():
                        print("I am inner function")
                    def inner2():
                        print("I am inner function")
                    inner1()
                    inner2()
                outer()

                OUTPUT:
                    I am outer function
                    I am inner function
                    I am inner function

            ->If call the local function outside the outer function then it will throw the error.
            NOTE: If the function is called before the declaration then it will throw unbound local error.
            NOTE: We can declare n number of functions inside the scope of another function.
            NOTE: We can call the inner function in a sequence of random ordered manner.

        ->MISCELLANEOUS FUNCTIONS:

            ->

        ->LAMDA FUNCTION OR ANONYMOUS FUNCTION:

            ->




->PILLARS OF OOPS:

    ->There are 4 main pillers in oops,
        ->ENCAPSULATION
        ->INHERITANCE
        ->POLIMORPHISM
        ->ABSTRACTION

    ->ENCAPSULATION:

        ->Encapsulation is the process of unwrapping data (variables) and methods (functions) together into a single unit is calles Encapsulation.
        ->It hides internal details and allows controlled access to the data. 
        ->MAIN USES OF ENCAPSULATION:
            ->Data Hiding/Security:
                ->Prevents direct access to internal variable.
                ->Protects data from accidental or unauthorized changes.
            ->Controlled Access:
                ->Data can only be accessed or modified using getters and setters or @property methods.
                ->You can control how the data is used or updated.
            ->Organization:
                ->Groups data and methods together in a single unit(class)
                ->Makes the code cleaner, organized and easier to manage.

        ->EXAMPLE:
            class bank:
                bankname="SBI"
                branch="VADA"
                ifsc="SBIN000123"
                def __init__(self,name,age,acc_no,pin,balance,mob):
                    self.name=name
                    self.age=age
                    self.acc_no=acc_no
                    self.__pin=pin
                    self.__balance=balance
                    self.mob=mob
                def cust_dt(self):
                    print(f'Bankname----->{self.bankname}')
                    print(f'Name----->{self.name}')
                    print(f'Age----->{self.age}')
                    print(f'Balance----->{self.__balance}')
            c1=bank("Gogul",22,948867,1234,5000,8825743920)
            c1.cust_dt()

    ->ACCESS SPECIFIERS:
        ->*Access -----> Permission.
        ->*Specifiers ----->Which tell something.
        ->Access specifiers are classified into 3 types:
            ->Public(No underscore)
            ->Protected(Single Underscore)
            ->Private(Double Underscore)
                ->These are the members of a class which define whether variables and methods can be accessed inside or outside the class.
                ->They specify whether a user or an object can acces the class members from outside the class or not.

        ->PUBLIC ACCESS SPECIFIER:
            ->It is a type of access specifier.
            ->It is a member of a class which will allows the user to access them
            ->They control access at different levels:
                ->Within the class.
                ->Outside the class.
                ->within the same module.
                ->Outside the module in another module.
                ->within the same package.
                ->outside the package in another package.
            ->Important point:
                ->Generally whatever is stored inside a class is treated as public access specifier by default.There is no need to do any extra work to specific public access.
            
        ->PROTECTED ACCESS SPECIFIERS:
            ->It is a type of access specifier.
            ->It a member of a class which allows access within the class and its derived (child) classes
            ->Protected member are defined by prefixing underscore(-) to the variable or method name a single
            ->They Control access at different level such as
                ->within the class- Allowed
                ->outside the class - Not recommended
                ->within the same module - Allowed
                ->outside the module in another module - Allowed but discouraged
                ->within the same package Allowed
                ->outside the package in another package - Allowed but discouraged
            Important Point:
                ->protected access specifier in not strictly, enforced in Python
                ->It is a convention, not a rule
                ->members prefixed with a single underscore (-) Indicate that they should be accessed only inside the class or it's child classes.
                ->Programmers should avoid accessing Protected members directly outside the class
        
        ->PRIVATE ACCESS SPECIFIER:
            ->It is a type of access specifier.
            ->Public and private access specifiers do not provide complete security to the members.To overcome this problem we use private access specifiers.
'''
'''
class student:
    inst="Qspiders"
    loc="vada"
    def __init__(self,name,age,course):
        self.__name=name
        self.__age=age
        self.__course=course
    def get_data(self):
        print("Name:",self.__name)
        print("Age:",self.__age)
        print("course",self.__course)
    def set_data(self,name,age,course):
        self.__name=name
        self.__age=age
        self.__course=course
obj=student('Mahi',22,'DSA')
obj.get_data()
obj.set_data('Dinga',12,'python')
obj.get_data()
'''

"""                                                        15/06/2026                                                        """

"""
       ->@PROPERTY IN PYTHON:
            ->@property is a decorator in Python used to access and modify private members of a class in a controlled and pythonic way without explicitly calling getter and setter methods
            ->EXAMPLE:
                    class student:
                        inst="Qspiders"
                        loc="vada"
                        def __init__(self,name,age,course):
                            self.__name=name
                            self.__age=age
                            self.__course=course
                        @property
                        def get_data(self):
                            print("Name:",self.__name)
                            print("Age:",self.__age)
                            print("course",self.__course)
                        @get_data.setter
                        def set_data(self,values):
                            self.__name=values[0]
                            self.__age=values[1]
                            self.__course=values[2]
                    obj=student('Mahi',22,'DSA')
                    obj.get_data
                    obj.set_data=('Dinga',12,'python')
                    obj.get_data

            ->EXAMPLE:
                class Bean:
                    def __init__(self,name,age):
                        self.__name=name
                        self.__age=age
                    @property
                    def name(self):
                        return self.__name
                    @name.setter
                    def name(self,value):
                        self.__name=value
                    @property
                    def age(self):
                        return self.__age
                    @age.setter
                    def age(self,value):
                        self.__age=value
                obj=Bean('Mahesh',16)
                print(obj.name)
                print(obj.age)
                obj.name='zoro'
                obj.age=21
                print(obj.name)
                print(obj.age)
            ->NOTE:
                ->In getters/setters, we call methods with paranthesis to get or set private data.
                ->In @property, we can use normal variable style - No paranthesis needed - to access or change private data safely.

"""

"""                                                        16/06/2026                                                        """

"""



"""

