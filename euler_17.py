"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

import time
t1 = time.time()

def num_to_words(x):
    values = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',
            13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',
            60:'sixty',70:'seventy',80:'eighty',90:'ninety',1000:'onethousand'}
    if x not in values:
        first = x//100
        second = ((x-first*100) // 10)*10
        third = (x - first*100) - second
        if first != 0:
            if second != 0 or third != 0:
                if second != 10:
                    score = values[first]+''+'hundred'+'and'+values[second]+''+values[third]
                else:
                    score = values[first]+''+'hundred'+'and'+values[second + third]
            else:
                score = values[first]+''+'hundred'
        else:
            score = values[second]+''+values[third]
        return score
    else:
        return values[x]

winner = 0

for x in range(1,1001):
    winner += len(num_to_words(x))

print(winner)
print(time.time() - t1)
