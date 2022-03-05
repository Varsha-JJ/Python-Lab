print("Enter three numbers\n")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))
num3 = int(input("Enter third number:"))

if num1 > num2 and num1 > num3:
    print("largest number is", num1)
elif num2 > num1 and num2 > num3:
    print("largest number is", num2)
else:
    print("largest number is:", num3)

