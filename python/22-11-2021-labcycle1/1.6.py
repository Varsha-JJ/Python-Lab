list1 = ["green", "blue", "orange", "purple"]
list2 = ["orange", "violet", "pink", "grey"]
print("The orginal list1 =",  str(list1))
print("The orginal list2 =",  str(list2))
result = [element for element in list1]
for a in list2:
    if a in list1:
        result.remove(a)
print("colors from list1 not contained in list2 is:", result)