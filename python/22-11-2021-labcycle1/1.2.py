print("Enter three numbers:")
num1 = input(int())
num2 = input(int())
num3 = input(int())

if num1 > num2 and num1 > num3:
    print("largest number is", num1)
elif num2 > num1 and num2 > num3:
    print("largest number is", num2)
else:
    print("largest number is:", num3)

