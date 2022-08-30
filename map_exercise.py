import math

# Suppose we have a list of items
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# An approach to getting only the prices will be as follows:
# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)

# Another way is to use the map function
# x = map(lambda item: item[1], items)
# # print(x)
# for item in x:
#     print(item)

# Alternatively
# Converting the map object to a list object
# prices = list(map(lambda item: item[1], items))
# print(prices)

# Suppose we want to calculate the area of a circle
# We start by creating a function


# def area(r):
#     """Area of a circle with radius r"""
#     return math.pi * (r**2)


# What if we need to compute the areas for many different circles
radii = [2, 5, 7.1, 0.3, 10]
# Method 1
# areas = []
# for r in radii:
#     a = area(r)
#     areas.append(a)

# print(areas)

# method 2: Using a map function
# areas_map = map(area, radii)
# print(areas_map)
# print(map(area, radii))
# Convert our map object to a list
# print(list(map(area, radii)))


# method 3: using a map function with lambda expression
# areas_map = map(lambda r: math.pi * (r**2), radii)
# print(list(areas_map))


# Another example
# Each city contains a tuple with name of the city and temperature in celsius
# from a weather map. Our goal is to convert this to a list where the degrees are in #fahrenheit. formula =(9/5) * C + 32
temps = [("Berlin", 29), ("Cairo", 36),
         ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]

# writing a converter function


# celsius_to_fahrenheit = lambda data:(data[0], (9/5)*data[1] + 32)

# cities_fahrenheit = lambda data:(data[0], (9/5)*data[1] + 32)
# print(list(map(cities_fahrenheit, temps)))
# print(list(map(cities_fahrenheit, temps)))
# Alternatively
# cities_fahrenheit = list(
#     map(lambda data: (data[0], (9/5)*data[1] + 32), temps))
# print(cities_fahrenheit)
