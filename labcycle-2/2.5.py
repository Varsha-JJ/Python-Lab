


#without function

a = input("Enter a word:")
char = a[0]
a = a.replace(char, "$")
a= char + a[1:]
print(a)