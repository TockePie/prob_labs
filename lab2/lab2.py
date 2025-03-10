import numpy as np

M = 1  # математичне сподівання
SIGMA = 4  # середньоквадратичне відхилення
N = 5000  # кількість значень
LOWER_BOUND = M - SIGMA # нижня межа
UPPER_BOUND = M + SIGMA # верхня межа

# Генерація випадкових чисел за нормальним (12) методом
uniform_samples = np.random.rand(N, 12)  # 12 рівномірних випадкових чисел для кожного значення
Y = np.sum(uniform_samples, axis=1) - 6  # Метод нормального (12)
R = M + SIGMA * Y  # Масштабування

# Обчислення статистичних параметрів
experimental_mean = np.mean(R)
experimental_std = np.std(R)

P_experimental = np.mean((R >= LOWER_BOUND) & (R <= UPPER_BOUND))

print(f"Теоретичне математичне очікування: {M}")
print(f"Експериментальне математичне очікування: {experimental_mean:.4f}")
print(f"Теоретичне середньоквадратичне відхилення: {SIGMA}")
print(f"Експериментальне середньоквадратичне відхилення: {experimental_std:.4f}")
print(f"Ймовірність P (експериментальна): {P_experimental:.4f}")
