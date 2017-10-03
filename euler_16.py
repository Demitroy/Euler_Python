# Find sum of the digits in 2 to power of 1000

import time
t1 = time.time()

score = 0
target = 2**1000
for x in str(target):
    score = score + int(x)

print(score)
print(time.time() - t1)
