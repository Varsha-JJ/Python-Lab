print("COMPOUND INTEREST")
p = float(input("Enter the principle amount:"))
r = float(input("Enter the rate of interest:"))
t = float(input("Enter the time span:"))
amount = p * (pow((1 + r / 100), t))
print("Compound interest is:", amount)