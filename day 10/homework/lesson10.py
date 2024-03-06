for i in range(20 + 1):
    print(i)

sum = 0

for i in range(50, 100+ 1):
    print(i)
    sum = sum + i

print(sum)

for i in range(-10, 10 + 1, 3):
    print(i)

num_1 = float(input("Enter First Number: "))
num_2 = float(input("Enter Second Number: "))

if num_1 > num_2:
    largest = num_1
    smallest = num_2

else:
    largest = num_2
    smallest = num_1

print("Value Goes From", smallest, "To" ,largest, "By 2")
for i in range(int(smallest), int(largest) + 1, 2):
    print(i)


sum = 0

num1 = float(input("Enter The Frist Number: "))
num2 = float(input("Enter The Second Number: "))

if num1 > num2:
    largest = num1
    smallest = num2

else:
    largest = num2
    smallest = num1

for i in range(int(smallest), int(largest) + 1):
    print(i)
    sum = sum + i

print(sum)


