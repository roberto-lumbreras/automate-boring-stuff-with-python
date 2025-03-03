#Lets find out the chance of having a streak of 6 heads or tails over 100 coin flips
import random
streaks = 0
for i in range (10_000):
    result = []
    for i in range(100):
        result.append(random.randint(0,1))
    for i in range(5,100,1):
        if (result[i-5]==result[i-4] and
         result[i-4]==result[i-3] and
         result[i-3]==result[i-2] and
         result[i-2]==result[i-1] and
         result[i-1]==result[i]):
            streaks+=1
            break
chance = streaks / 10_000
print('Chance of having a streak of 6 in 100 coin flips is '+str(chance))

