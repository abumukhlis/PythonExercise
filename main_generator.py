# Generator expressions
from sys import getsizeof
# generator comparison to list
values = [x*2 for x in range(100000)]
print('list:', getsizeof(values))

values = (x*2 for x in range(100000))
print("gen: ", getsizeof(values))
