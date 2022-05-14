import time # Импортируем библиотеку time.
import re # Импортируем библиотеку re.
try:
    filePath = input('Введите путь к файлу: ') # Получаем путь к файлу.
    with open(filePath, 'r', encoding='utf8') as file: # Безопасно открываем файл.
        k = int(input('Введите K: ')) # Получаем K.
        print('Результат работы программы: ')
        for line in file: # Читаем файл построчно.
            numbers = re.sub(r'[^\w\s]',' ', line).split() # Получаем список чисел в строке.
            for number in numbers: # Перебираем список чисел строки.
                if (number.isnumeric() and len(number) <= k): # Проверяем элементы на соответствие условию задания.
                    print(number)
        print("Время выполнения: " + str(time.process_time())) # Высчитываем время работы программы.
except FileNotFoundError:
    print('Файл *.txt не обнаружен.')
    print("Время выполнения: " + str(time.process_time()))
except ValueError:
    print('Вы ввели некорректное значение.')
    print("Время выполнения: " + str(time.process_time()))