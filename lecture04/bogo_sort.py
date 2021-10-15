import random

numbers = [6, 3, 2, 8, 9, 7, 5, 4, 1]
print(numbers)

random.shuffle(numbers)
while numbers != sorted(numbers):
    random.shuffle(numbers)

print(numbers)