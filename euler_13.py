# Find first 10 digits of sum of given 100 50 digit numbers.

import time
t1 = time.time()

nums = []

inp = open("large_sum.txt",'r')
for line in inp.readlines():
    for i in line.split():
        nums.append(int(i))
inp.close()

winner = str(sum(nums))[:10]

print(winner)
print(time.time() - t1)
