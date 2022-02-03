start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)