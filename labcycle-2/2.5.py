def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, "$")
    str1 = char + str1[1:]
    return str1


print(change_char("malayalam"))


#without function

a = input("Enter a word:")
char = a[0]
a = a.replace(char, "$")
a= char + a[1:]
print(a)