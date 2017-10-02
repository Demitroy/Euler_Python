# Find the largest prime factor of 600851475143

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

target = 600851475143

for x in range(2,int(target**(1/2))):
    if target%x == 0:
        target = target/x
    if is_prime(target):
        break

print(target)
print(time.time() - t1)
