n = int(input("Enter the limit:"))
list1 = []
print("Enter the values:")
for i in range(0,n):
    m = int(input())
    list1.append(m)
print("list is:",list1)
list2 = []
for i in list1:
    if i%2!=0:
        list2.append(i)
print("list after removing even numbers is:",list2)
