#First Homework

num = int(input("Please enter number: "))

if num > 0:
    print("Number Is Positive")
elif num < 0:
    print("Number Is Negative")
else:
    print("Number Is Zero")

#First Homework
    
#Second Homework
    
num = float(input("Please choose 1 or 2: "))
num2 = float(input("Please enter number: "))

if num > 0 and num < 2:
    print(num2 / 1.6)
elif num > 1 and num < 3:
    print(num2 * 1.6)
else:
    print("Wrong Decision")

#Second Homework

#Third Homework

name = input("Please enter your username: ")

lastname = input("Please enter your lastname: ")

age = input("Please enter your age: ")

email = input("Please enter your email: ")

print(name + " " + lastname + " " + age  + " " + email)

#Third Homework

#Fourth Homework

num = float(input("Please enter first number: "))
num1 = float(input("Please enter second number: "))
num2 = float(input("Please enter third number: "))

sum = (num + num1 + num2)

print(sum / 3)

#Fourth Homework

#Fiveth Homework

num = int(input("Please enter number in ragne 1, 9: "))


for i in range(num, 50 + 1):
    if num >= 1 and num <= 9:
        print(i)

if num > 9:
    print("Wrong Decision")

#Fiveth Homework

#Sixth Homework

num_1 = float(input("Enter First Number: "))
num_2 = float(input("Enter Second Number: "))

if num_1 > num_2:
    largest = num_1
    smallest = num_2

else:
    largest = num_2
    smallest = num_1

cub = num_1 + num_2 ** 2

for i in range(int(smallest), int(largest) + 1):
    print(i)
    cub = cub + i

print(cub)

#Sixth Homework

#Seventh Homework

num = int(input("Please enter two digit number: "))

sum = 0

for i in range(num + 1):
    if num > 9 and num < 100:
        print(i)
    sum = sum + i

print(sum)

#Seventh Homework

#Eighth Homework

num = int(input("Please enter number: "))

x0 = num * 0
x1 = num * 1
x2 = num * 2
x3 = num * 3
x4 = num * 4
x5 = num * 5
x6 = num * 6
x7 = num * 7
x8 = num * 8
x9 = num * 9

print(num + x0)
print(num + x1)
print(num + x2)
print(num + x3)
print(num + x4)
print(num + x5)
print(num + x6)
print(num + x7)
print(num + x8)
print(num + x9)

#Eighth Homework

#Nineth Homework

num = float(input("Please enter number: "))
num1 = float(input("Please enter second number "))
choose = input("Please choose operation: ")

devide = num / num1
multiply = num * num1
plus = num + num1
minus = num - num1

if choose == devide:
    print(devide)
elif choose != multiply:
    print(multiply)
elif choose != plus:
    print(plus)
elif choose != minus:
    print(minus)
else:
    print("Try Again")

FAILED_HOMEWORK = True

#Nineth Homework

#Tenth Homework

name = input("Please enter name: ")
num = int(input("Please enter number of multiply: "))

for i in range(num):
    print(name)

#Tenth Homework

weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
age = int(input("Please enter your age: "))

weight_to_pounds = weight * 1.2

print(weight + weight_to_pounds)
print(height / 100)

if age > 50:
    print("You are old")
elif age <= 50 and age >= 18:
    print("you are adult")
else:
    print("you are kid")

#Tenth Homework

#Eleventh Homework

num = int(input("Please enter number between 1, 5: "))

if num > 0 and num < 6:
    print("Valid Input")
else:
    print("Invalid Input")
    
#Eleventh Homework








