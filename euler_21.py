# Find the sum of amicable numbers up to 10000

import time
t1 = time.time()

def get_divisors(x):
    return sum([i for i in range(1,int(x/2)+1) if x%i == 0])

winner = 0

for x in range(10000):
    check = get_divisors(x)
    if x == get_divisors(check) and x != check:
        winner += x

print(winner)
print(time.time() -t1)
