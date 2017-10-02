# Find the sum of all primes below 2000000

import time
t1 = time.time()

def is_prime(x):
    if x == 2 or x == 3: return True
    if x < 2 or x%2 == 0: return False
    if x < 9: return True
    if x%3 == 0: return False
    r = int(x**0.5)
    f = 5
    while f <= r:
        if x%f == 0: return False
        if x%(f+2) == 0: return False
        f = f + 6
    return True

prims = [x for x in range(1, 2000000) if is_prime(x)]

print(sum(prims))
print(time.time() - t1)
