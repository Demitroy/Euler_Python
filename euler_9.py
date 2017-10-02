# Find pythagorean triple where a + b + c = 1000

import time
t1 = time.time()

for a in range(1,500):
    for b in range(a,1000):
        if((a**2 + b**2)**(1/2))%1 == 0 and a+b+(a**2 + b**2)**(1/2) == 1000:
            print(a*b*(a**2+b**2)**(1/2))

print(time.time() - t1)
