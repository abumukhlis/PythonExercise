# List comprehension Examples

# Example 1
# To get the square of numbers between (1, 100)
squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

# Example 2
# To get the remainders when divided by 5 and 11
remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

# Example 3
# To get titles starting with letter G from list of movies
movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption",
          "Toy Story", "Gone with the Wind", "Citizen Cane",
          "It's a wonderful Life",
          "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters",
          "To Kill a Mockingbird", "Good Will Hunting",
          "2001: A Space odyssey", "Raiders of the Lost Ark", "Groundhog Day",
          "Close Encounters of the Third Kind"]
# Using for loop
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)
# using list comprehension
gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2)

# Example 4
# To get the list of titles of the movies released before year 2000
movies2 = [("Citizen Cane", 1941), ("Spirited Away", 2001),
           ("It's a wonderful Life", 1946), ("Gattaca", 1997),
           ("No Country for Old Men", 2007), ("Rear Window", 1954),
           ("The Lord of the Rings: The Fellowship of the Ring", 2001),
           ("Groundhog Day", 1993),
           ("Close Encounters of the Third Kind", 1977),
           ("The Royal Tenenbaums", 2001),
           ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

before_2000 = [title for (title, year) in movies2 if year < 2000]
print(before_2000)

# Example 5
# Scalar Multiplication
v = [2, -3, 1]
w = [4*x for x in v]
print(w)

# Example 6
# Using Cartesian Product
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)
