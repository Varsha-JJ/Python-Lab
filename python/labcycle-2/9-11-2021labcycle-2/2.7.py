list = [ ]
n = int(input("Enter number of elements to be inserted:"))
for i in range (0,n):
    elem = int(input())
    list.append(elem)
list.reverse()
print("After reversing the list will be:")
for x in list:
 print(x)

#subject = ["malayalam", "english", "hindi"]
#subject.reverse()
#for y in subject:
 #   print(y)