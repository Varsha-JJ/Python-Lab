st=int(input("Enter the intial range(four digit number):"))
if(st<1000):
    print("enter a 4 dig num")
    st = int(input("Enter the intial range:"))
end=int(input("Enter the End range(four digit number):"))
if(end<st):
    print("Enter a value greater than inital range:")
    end = int(input("Enter the End range:"))
print("Perfect squares and even numbers in the range"+str(st)+"-"+str(end)+":")
for i in range(st,end):
    if i%2==0 and i**(1/2)==int(i**(1/2)):
        print(i)
