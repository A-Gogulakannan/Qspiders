'''

1) Write a python program to 

n=4
for i in range(n):
    for j in range(n):
        if i==n-1 or i+j==n-1 :
            print("*", end='')
        else: 
            print(" ",end='')
print()

2) hallow pyramid, right hallow triangle, top hallow triangle

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