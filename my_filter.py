import statistics
# Filter the list for items greater than or equal to $10
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# filtered = filter(lambda item: item[1] >= 10, items)
# print(list(filtered))
# # Or this way
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)

# Another example:
# To find all data above average
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)
# We need data greater than the average
greater_than_average = list(filter(lambda d: d > avg, data))
print(greater_than_average)  # We get the three values above the mean

# Values lower than the average
lower_than_average = list(filter(lambda d: d < avg, data))
print(lower_than_average)

# Another example
# To remove missing data from the list below
countries = ["", "Argentina", "", "Brazil",
             "Chile", "", "Columbia", "", "Ecuador", "", "", "Venezuela"]

filtered_countries = list(filter(None, countries))
print(filtered_countries)
