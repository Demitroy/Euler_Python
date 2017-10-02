# Find smallest integer divisble by integers from 1 to 20

import time
t1 = time.time()

def is_target(x):
    if x%20 == 0 and x%19 == 0 and x%18 == 0 and x%17 == 0 and x%16 == 0 and x%15 == 0 and x%14 == 0 and x%13==0 and x%12 == 0 and x%11 == 0 and x%9 == 0:
        return True
    return False

x = 20

while is_target(x) == False:
    x += 20

print(x)
print(time.time() - t1)
