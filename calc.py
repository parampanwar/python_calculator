import sys
print("Enter your choice: ")
print("1. for addition ")
print("2. for subtraction ")
print("3. for multiplication ")
print("4. for division ")
n = int(input())

if n not in [1,2,3,4]:
    print("Invalid Choice")
    sys.exit()

print("Enter Two Digits: ")
a, b = map(int, input().split())

c = 0

if n == 1:
    c = a+b
    print(c)
elif n == 2: 
    c = a-b
    print(c)
elif n == 3:
    c = a * b
    print(c)
elif n == 4:
    if b != 0:
        c = a//b
        print(c)
    else: 
        print("Division by zero!")
else:
    print("Invalid Choice")

