list1=[20,60,30,12,90,15]
list2=[50,15,48,90]
print("length of list1 :",list1)
print("length of list2 :",list2)
if len(list1)==len(list2):
    print("Two lists are of same length")
else:
    print("Two lists are of different length")
total = sum(list1)
print("sum of list1 :",total)
total = sum(list2)
print("sum of list2 :",total)
if sum(list1)==sum(list2):
    print("Two lists sum is equal")
print("Value occur in both:")
for i in list1:
   if i in list2:
        print(i)
