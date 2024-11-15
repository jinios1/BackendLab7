# Шаг 1: Формирование строки с подстановкой значений
def formatted_string(param1, param2, param3):
    """
    Шаг 1: Функция принимает минимум 3 параметра и возвращает строку с подставленными значениями.
    1.1 - param1 - строка
    1.2 - param2 - результат арифметической операции
    1.3 - param3 - результат вызова другой функции
    """
    predefined_string = "Hello, {0}! The result of the operation is {1} and here is a value: {2}."
    return predefined_string.format(param1, param2 * 2, param3())

# Вспомогательная функция для шага 1
def additional_value():
    """Функция, которая возвращает фиксированное значение."""
    return 42

# Шаг 2: Повторение комбинации строк
def repeat_strings(string1, string2, count):
    """
    Шаг 2: Функция формирует строку из повторений комбинации двух строк и выводит результат,
    каждое повторение на новой строке.
    """
    combination = f"{string1} {string2}"
    result = (combination + "\n") * count
    print(result.strip())

# Шаг 3: Подсчёт вхождений подстроки без учёта регистра
def count_substring_occurrences(main_string, substring):
    """
    Шаг 3: Функция считает количество вхождений подстроки в строку без учёта регистра.
    """
    return main_string.lower().count(substring.lower())

# Шаг 4: Извлечение подстроки по индексам
def extract_substring(s, start, end):
    """Шаг 4: Функция возвращает подстроку между индексами (в одну строку)."""
    return s[start:end]

# Шаг 5: Поиск слов с латинскими буквами
def find_words_with_latin(*strings):
    """
    Шаг 5: Функция ищет слова с латинскими буквами в произвольном количестве строк.
    Возвращает строки с такими словами и количество найденных слов.
    """
    latin_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    detected_strings = []
    total_count = 0

    for string in strings:
        words = string.split()
        found_words = [word for word in words if any(char in latin_letters for char in word)]
        if found_words:
            detected_strings.append(string)
            total_count += len(found_words)

    return detected_strings, total_count

# Шаг 6: Проверка на палиндром
def is_palindrome(s):
    """
    Шаг 6: Функция определяет, является ли строка палиндромом.
    Игнорируются пробелы, знаки препинания и регистр.
    """
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Шаг 7: Удаление лишних пробелов
def trim_and_measure(s):
    """
    Шаг 7: Функция удаляет лишние пробелы из строки и возвращает её длину.
    """
    return len(' '.join(s.split()))

# Шаг 8: Замена символов окончания предложения
def replace_sentence_endings(s):
    """
    Шаг 8: Функция заменяет символы окончания предложений на символы переноса строки.
    """
    import re
    return re.sub(r'[.!?]', '\n', s)

# Шаг 9.1: Преобразование строки в "змеиный_регистр"
def to_snake_case(s):
    """
    Шаг 9.1: Функция преобразует строку в "змеиный_регистр".
    """
    import re
    s = re.sub(r'[\s\-]', '_', s.strip())
    return s.lower()

# Шаг 9.2: Удаление всех цифр из строки
def remove_digits(s):
    """
    Шаг 9.2: Функция удаляет все цифры из строки.
    """
    return ''.join(char for char in s if not char.isdigit())

# Шаг 9.3: Перестановка слов в строке в обратном порядке
def reverse_words_order(s):
    """
    Шаг 9.3: Функция переставляет слова в строке в обратном порядке.
    """
    return ' '.join(s.split()[::-1])
