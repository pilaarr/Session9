import random

sum = 0
for i in range(10):
    sum += random.randint(-50, 50)

print(f"The random sum is: {sum}")