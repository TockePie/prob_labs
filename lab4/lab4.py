import numpy as np
from scipy.stats import chi2

# Параметри
SIGMA_0 = 1
SIGMA_1 = 2
ALPHA = 0.05
N = 10**4  # Розмір вибірки для кожної гіпотези

# Критичне значення c (з теоретичного розрахунку)
c = SIGMA_0**2 * chi2.ppf(1 - ALPHA, df=1)
print(f"Критичне значення c: {c:.3f}")

# Генерація вибірок
np.random.seed(42)  # Для відтворюваності
sample_H0 = np.random.normal(0, SIGMA_0, N)  # H0: N(0, 1)
sample_H1 = np.random.normal(0, SIGMA_1, N)  # H1: N(0, 4)

# Обчислення квадратів значень
v_sq_H0 = sample_H0**2
v_sq_H1 = sample_H1**2

# Класифікація за критерієм Неймана-Пірсона
# Відхилити H0, якщо v² > c
reject_H0 = v_sq_H0 > c
accept_H1 = v_sq_H1 <= c

# Емпіричні ймовірності помилок
empirical_alpha = np.mean(reject_H0)  # Помилка першого роду
empirical_beta = np.mean(accept_H1)   # Помилка другого роду

# Теоретичні значення
theoretical_alpha = ALPHA
theoretical_beta = chi2.cdf(c / SIGMA_1**2, df=1)  # P(v² <= c | H1)

# Вивід результатів
print("\nРезультати:")
print(f"Емпірична α (пом. 1-го роду): {empirical_alpha:.4f} (теоретична: {theoretical_alpha:.2f})")
print(f"Емпірична β (пом. 2-го роду): {empirical_beta:.4f} (теоретична: {theoretical_beta:.2f})")
