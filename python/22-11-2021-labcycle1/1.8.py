list = [1, 2, 3, 6, 9, 10, 15, 20, 11]
print("The list of elements before  removing even:", list)
for i in list:
    if i % 2 == 0:
        list.remove(i)
print("The list of elements after removing even:", list)