#Test

import random

total :int = 0

for _ in range(1000):
    total += sum(random.randint(0, 1) for _ in range(10000))

print(total / 1000)