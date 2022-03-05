n = int(input("Enter the limit:"))
m1 = 0
m2 = 1
s = 0
print("Fibonacci series:")
print(m1)
print(m2)
for i in range(1,n-1):
    s = m1 + m2
    m1 = m2
    m2 = s
    print(s)
