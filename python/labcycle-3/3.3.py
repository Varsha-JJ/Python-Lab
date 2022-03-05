list1 = [ ]
n = int(input("Enter number of elements:"))
for i in range(0,n):
    elem = int(input())
    list1.append(elem)
total = 0
for x in range(0, len(list1)):
    total = total + list1[x]

print("Sum of all elements in given list: ", total)