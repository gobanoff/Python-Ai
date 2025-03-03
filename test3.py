import numpy as np
"""
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Двумерный массив (матрица)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Массив из нулей
zeros = np.zeros((3, 3))
print(zeros)

# Массив из единиц
ones = np.ones((2, 4))
print(ones)

# Случайный массив
rand_arr = np.random.rand(3, 3)
print(rand_arr)
"""

"""
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Арифметические операции
print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)  # [4 10 18]
print(a / b)  # [0.25 0.4  0.5 ]

# Математические функции
print(np.sin(a))  # Синус каждого элемента
print(np.log(a))  # Натуральный логарифм
print(np.exp(a))  # Экспонента

"""

"""
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # (2, 3) — 2 строки, 3 столбца
print(arr.size)   # 6 элементов
print(arr.ndim)   # 2D массив



arr = np.array([[10, 20, 30], [40, 50, 60]])

# Доступ к элементам
print(arr[0, 1])  # 20
print(arr[1, :])  # [40 50 60] — вся вторая строка
print(arr[:, 2])  # [30 60] — все элементы третьего столбца

arr = np.array([10, 20, 30, 40, 50])

print(np.mean(arr))  # Среднее: 30.0
print(np.median(arr))  # Медиана: 30.0
print(np.std(arr))  # Стандартное отклонение
print(np.min(arr))  # Минимум: 10
print(np.max(arr))  # Максимум: 50

"""

temps = np.array([25.3, 26.1, 24.8, 27.5, 28.0, 29.3, 26.7])
print(f"Средняя температура: {np.mean(temps)}°C")  #  26.814285714285713°C