list1=[2,3,4]
list2=[1,3,5]
flag=1
for i in list1:
    for j in list2:
        if(i==j):
            print(i)
            flag=1
            exit(0)
        else:
            flag=0
            if(flag==0):
                print("not equal")