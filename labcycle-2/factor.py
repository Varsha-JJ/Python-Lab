num = int(input("Enter a number:"))
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("Factorial is:",fact)
factorial(num)
