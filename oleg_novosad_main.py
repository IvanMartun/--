import random
import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('game.db')
c = conn.cursor()

# Створення таблиці для зберігання результатів
c.execute('''CREATE TABLE IF NOT EXISTS results
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              difficulty TEXT,
              moves INTEGER)''')

# Список допустимих рівнів складності
difficulty_levels = ['легкий', 'середній', 'складний']

# Функція, що генерує карту заданого розміру
def generate_map(size):
    # Створення порожньої карти
    map = [[None for x in range(size)] for y in range(size)]

    # Генерація координат скарбу та інших предметів
    treasure_x, treasure_y = random.randint(0, size - 1), random.randint(0, size - 1)
    water1_x, water1_y = random.randint(0, size - 1), random.randint(0, size - 1)
    water2_x, water2_y = random.randint(0, size - 1), random.randint(0, size - 1)
    animal_x, animal_y = None, None
    if size >= 10:
        animal_x, animal_y = random.randint(0, size - 1), random.randint(0, size - 1)
    key_x, key_y = None, None
    if size >= 20:
        key_x, key_y = random.randint(0, size - 1), random.randint(0, size - 1)
    shovel_x, shovel_y = None, None
    if size >= 10:
        shovel_x, shovel_y = random.randint(0, size - 1), random.randint(0, size - 1)

    # Заповнення карти предметами
    for y in range(size):
        for x in range(size):
            if x == treasure_x and y == treasure_y:
                map[y][x] = 'СКАРБ'
            elif x == water1_x and y == water1_y:
                map[y][x] = 'ВОДА'
            elif x == water2_x and y == water2_y:
                map[y][x] = 'ВОДА'
            elif x == animal_x and y == animal_y:
                map[y][x] = 'ЗВІР'
            elif x == key_x and y == key_y:
                map[y][x] = 'КЛЮЧ'
            elif x == shovel_x and y == shovel_y:
                map[y][x] = 'ЛОПАТА'
            else:
                map[y][x] = 'ПОЛЕ'
    