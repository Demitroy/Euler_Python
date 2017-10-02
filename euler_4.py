# Find largest palindrom made of two three-digit numbers

import time
t1 = time.time()

winner = max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])

print(winner)
print(time.time() - t1)
