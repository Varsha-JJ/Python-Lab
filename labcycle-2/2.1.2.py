n = int(input("Enter nth number : "))
sum = 0
for s in range(1, n + 1):
    sum = sum + (s * s)
print("Sum of squares is : ", sum)
