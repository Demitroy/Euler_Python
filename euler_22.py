# Sort names, assign score based on A = 1, B = 2, etc, and multiply by position in sorted list.  Sum the list for the answer.

import time
t1 = time.time()

def name_score(name):
    points = 0
    for j in range(len(name)):
        points += letterscore[name[j]]
    return points

letterscore = {'\n':0,'"':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

score = 0
count = 0
with open('names.txt','r') as f:
    names_list = sorted(i for i in f.read().split(','))

for i in names_list:
    count += 1
    score += count*name_score(i)

print(score)
print(time.time()-t1)
