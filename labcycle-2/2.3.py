list1=list()
count=0
print("Enter a number: ")
n=int(input())
print("Enter ",n," first names:\n")
for i in range(0,n):
    list1.insert(i,str(input()))
for i in range(0,n):
    for j in list1[i]:
        if 'a'==j:
            count=count+1
print("The number of occurences of character 'a' in above list is: ",count)