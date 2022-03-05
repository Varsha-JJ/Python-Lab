t1 = {
    "name": "ammu",
    "age": 22,
}
t2 = {
    "place": "kottayam"
}
print("Dictionary 1:",t1)
print("Dictionary 2:",t2)
dict = t1.copy()
dict.update(t2)
print("After merging two dictionary:",dict)
