# Find the difference between the sums of the squares of the first 100 integers, and the square of the sums of the first 100 integers

import time
t1 = time.time()

sum_squares = sum([x**2 for x in range(101)])
square_sums = (sum([x for x in range(101)]))**2

print (square_sums - sum_squares)
print(time.time() - t1)
