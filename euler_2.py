# Sum of even Fibonacci numbers that are less than 4000000

import time
t1 = time.time()

fib = [1,2]
score = 2
while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])
    if fib[-1]%2 == 0:
        score += fib[-1]

print(score)
print(time.time() - t1)
