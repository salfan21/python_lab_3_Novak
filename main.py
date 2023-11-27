#1

import math

def gaussian_function(x, mu, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - mu)**2 / (2 * sigma**2))

# Задаємо параметри функції
mu = 0
sigma = 1

# Обчислюємо значення функції Гауса для конкретних x
x_values = [-2, -1, 0, 1, 2]
for x in x_values:
    result = gaussian_function(x, mu, sigma)
    print(f'f({x}) = {result}')

#2

# Створюємо змінні для кількості яблук у Джона, Мері і Адама
john = 3
mary = 5
adam = 6

# Виводимо значення змінних в один рядок, розділені комами
print(f"Кількість яблук у Джона, Мері і Адама: {john}, {mary}, {adam}")

# Створюємо нову змінну, яка містить суму кількостей яблук
total_apples = john + mary + adam

# Виводимо значення нової змінної в консоль
print(f"Загальна кількість яблук: {total_apples}")

#3

def miles_to_kilometers(miles):
    conversion_factor = 1.61
    kilometers = miles * conversion_factor
    return kilometers

def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles

# Вихідні дані
miles_value = 7.38
kilometers_value = 12.25

# Виклик функцій та виведення результатів
print(f"{miles_value} miles is {miles_to_kilometers(miles_value)} kilometers.")
print(f"{kilometers_value} kilometers is {kilometers_to_miles(kilometers_value)} miles.")

#4

x =  4
x = float(x)

y = 3 * x**3 - 2 * x**2 + 3 * x - 1

# виводимо результат
print("y =", y)

#5

# Призначення кількості годин
hours = 3
# Кількість секунд у 1 годині
seconds_per_hour = 3600
# Виведення кількості годин
print("Hours: ", hours)
# Обчислення та виведення кількості секунд у заданій кількості годин
print("Seconds in Hours: ", hours * seconds_per_hour)

#6

# введення значення a (число з плаваючою комою)
a = float(input("Введіть значення для a: "))

# введення значення b (число з плаваючою комою)
b = float(input("Введіть значення для b: "))

# результати основних арифметичних операцій
result_addition = a + b
result_subtraction = a - b
result_multiplication = a * b

# перевірка, чи b не рівне 0 перед діленням
if b != 0:
    result_division = a / b
    print("Результат ділення:", result_division)
else:
    print("Ділення на нуль не є визначеним.")

# виведення результатів
print("Результат додавання:", result_addition)
print("Результат віднімання:", result_subtraction)
print("Результат множення:", result_multiplication)

print("\nThat's all, folks!")

#7

from fractions import Fraction

def nested_fraction(x, depth):
    result = Fraction(1, x)
    for i in range(depth):
        result = Fraction(1, x + result)
    return result

# Тестові дані
test_data = [1, 10, 100, -5]

# Виведемо результати тестування
for x_value in test_data:
    result = nested_fraction(x_value, 5)  # Збільшив глибину вкладення до 5
    print(f"x = {x_value}, y = {float(result):.16f}")

def calculate_end_time(start_hour, start_minute, duration_minutes):
    total_minutes = (start_hour * 60 + start_minute + duration_minutes) % (24 * 60)
    end_hour = total_minutes // 60
    end_minute = total_minutes % 60
    return end_hour, end_minute

# Введення даних
hour = int(input("Введіть години початку (0-23): "))
mins = int(input("Введіть хвилини початку (0-59): "))
dura = int(input("Введіть тривалість в хвилинах: "))

# Розрахунок та виведення результату
end_hour, end_minute = calculate_end_time(hour, mins, dura)
print(f"Початок: {hour:02d}:{mins:02d}")
print(f"Тривалість: {dura} хвилин")
print(f"Кінець: {end_hour:02d}:{end_minute:02d}")