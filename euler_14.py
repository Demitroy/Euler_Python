"""
Find the longest string created by the following algorithm for any number less than 1 million.

n → n/2 (n is even)
n → 3n + 1 (n is odd)
"""

import time
t1 = time.time()

def factor_increase(x):
    factor_list = [x]
    while x > 1:
        if x % 2 == 0:
            factor_list.append(int(x/2))
            x = int(x/2)
        else:
            factor_list.append(int(3*x+1))
            x = int(3*x+1)
    return factor_list

winner = 0
score = 0

for x in range(500000,1000000):
    factor_list = factor_increase(x)
    if len(factor_list) > winner:
        winner = len(factor_list)
        score = x
        if winner > 500:
            break

print(winner, score)
print(time.time() - t1)
