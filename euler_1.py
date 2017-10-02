# Print the sum of natural numbers divisible by either 3 or 5, up to 1000.

import time
t1 = time.time()

print(sum([x for x in range(1000) if x%3 == 0 or x%5 == 0]))
print(time.time() - t1)
