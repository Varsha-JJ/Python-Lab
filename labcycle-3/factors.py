n = int(input("Enter a number:"))
def factor(num):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
print("Factors are:")
factor(n)
