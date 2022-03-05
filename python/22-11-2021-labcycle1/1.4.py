def merge(t1, t2):
    return (t2.update(t1))


t1 = {
    "name": "ammu",
    "age": 22,
}

t2 = {
    "place": "kottayam"
}
print(merge(t1, t2))
print(t2)