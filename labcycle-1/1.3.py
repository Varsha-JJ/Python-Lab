list1=list()
count=0
print("\n enter a number: ")
n=int(input())
print("\n enter ",n," names:\n")
for i in range(0,n):
    list1.insert(i,str(input()))
for i in range(0,n):
    for j in list1[i]:
        if 'a'==j:
            count=count+1
print("\n the number of occurences of character 'a' in above list is: ",count)