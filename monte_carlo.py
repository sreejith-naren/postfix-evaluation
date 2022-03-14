import random
from math import sqrt

random.seed(0)  

def Pi_estimation(n):
    circle = 0

    for i in range(1,n+1):
        x = random.random()
        y = random.random()
        
        if sqrt(x**2 + y**2) <= 1: #to check if the produced number is in the circle
            circle += 1

    Pi = 4 * (circle/n)
    return Pi

n=[10,100]#,1000,10000,100000,10000000,100000000,200000000]

Pi_storage =[]

for j in n:
    Pi_storage.append(Pi_estimation(j))

for k in range(len(n)):
    print(f'The reult of PI estimation after {n[k]} attempt is equal to: {Pi_storage[k]}')