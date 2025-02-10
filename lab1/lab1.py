import random

def count_matching_bits(a, b):
    xor = a ^ b
    return 8 - bin(xor).count('1')

N = 1000000
success = 0

for _ in range(N):
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    matches = count_matching_bits(a, b)
    if matches >= 4:
        success += 1

probability = success / N
print(f"Статистична ймовірність: {probability}")
