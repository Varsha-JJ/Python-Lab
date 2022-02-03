string = "apple"
print(string)
def change_sring(string):
    return string[-1:] + string[1:-1] + string[:1]
print(change_sring('apple'))