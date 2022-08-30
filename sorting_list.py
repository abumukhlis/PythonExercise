numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# numbers.sort(reverse=True)
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
# print(numbers)
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# Nothing happens when you use sort() for the tupple
# items.sort()
# print(items)

# Another way is to declare a function and then sort the tuple


# def sort_item(item):
#     return item[1]
#
#
# items.sort(key=sort_item)
# print(items)

# A better way is using lambda expression making it cleaner
# items.sort(key=lambda item: item[1])
# print(items)

scifi_authors = [
    "Isaac Asimov", "Ray Bradbury", "Robert Heinlein",
    "Artus C. Clarke", "Frank Herbert", "Orson Scot Card",
    "Douglas Adams", "H. G. Wells", "Leig Brackett"
]
# using sort() without condition
# scifi_authors.sort()
# print(scifi_authors)
# sorting by last name
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
