"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import time
t1 = time.time()

def factorial(x):
    score = 1
    for i in range(1,x+1):
        score = score*i
    return score

number = factorial(100)
score = 0

for x in str(number):
    score = score + int(x)

print(score)
print(time.time()-t1)
