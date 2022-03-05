n = int(input("Enter the limit:"))
list = []
print("Enter the values:")
for i in range(0, n):
    m = int(input())
    list.append(m)
print("list is:", list)
s = 0
for i in list:
    s = s + i
print("sum of list is:", s)
