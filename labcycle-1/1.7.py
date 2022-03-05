dict1 = {
    "month": "june",
    "Department": "computer science",
    "course": "mca",
}
list = list(dict1.items())
list.sort()
print("Ascending order is",list)
list.sort(reverse=True)
print("Descending order is",list)