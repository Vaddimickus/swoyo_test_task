from math import ceil


# Простые числа в заданном диапазоне.
# Необходимо разработать функцию prime_numbers(low, high), где low и high – нижняя и верхняя
# границы диапазона, в котором надо найти эти числа. Функция должна возвращать список с
# числами, отсортированными по возрастанию.
# Функция должна корректно обрабатывать некорректное значение аргументов, возвращая пустой
# список
def prime_numbers(low, high):
    try:
        low = float(low)
        high = float(high)
    except:
        return []
    if high < low:
        low, high = high, low
    low = int(low)
    high = int(ceil(high))
    result = []
    for i in range(low + 1, high):
        result.append(i)
    return result


# Статистика текста
# Необходимо разработать функцию text_stat(filename), которая по заданному имени файла
# рассчитывала статистику его содержимого. Статистика должна рассчитываться для следующих
# категорий:
# • Частота использования каждой буквы латинского или кириллического алфавита
# • Количество слов в тексте
# • Количество абзацев в тексте
# • Доля слов, в которых встречается конкретная буква. Если буква встречается в слове более
# одного раза, считать это одним попаданием буквы в слово
# • Количество слов, в которых одновременно встречаются буквы обоих алфавитов
# Функция должна возвращать словарь со следующим содержимым:
# • Ключ - буква алфавита, значение – tuple (частота_использования_буквы,
# доля_слов_с_буквой)
# • Ключ – word_amount, значение – количество слов в тексте
# • Ключ – paragraph_amount, значение – количество абзацев в тексте
# • Ключ – bilingual_word_amount, значение – количество слов с использованием букв из
# обоих алфавитов
# Функция должна корректно обрабатывать некорректное значение аргумента, возвращая словарь с
# ключом error и значением с кратким описанием проблемы
def text_stat(filename):
    try:
        f = open(filename)
        f.close()
    except Exception as error:
        return dict({"error": str(error)})

    result = dict()
    eng_alphabet = dict()
    rus_alphabet = dict()
    for i in 'abcdefghijklmnopqrstuvwxyz':
        eng_alphabet[i] = [0, 0]
    for i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        rus_alphabet[i] = [0, 0]

    with open(filename, encoding='utf-8') as f:
        text = ""
        for line in f.readlines():
            text += line.lower()
        for i in text:
            if i in eng_alphabet:
                eng_alphabet[i][0] += 1
            elif i in rus_alphabet:
                rus_alphabet[i][0] += 1

        words = text.split()
        result["word_amount"] = len(words)

        result["paragraph_amount"] = 1
        for i in text:
            if i == '\n':
                result["paragraph_amount"] += 1

        result["bilingual_word_amount"] = 0
        for word in words:
            eng_symbol = False
            rus_symbol = False
            for i in eng_alphabet:
                if i in word:
                    eng_alphabet[i][1] += 1
                    eng_symbol = True
            for i in rus_alphabet:
                if i in word:
                    rus_alphabet[i][1] += 1
                    rus_symbol = True
            if eng_symbol and rus_symbol:
                result["bilingual_word_amount"] += 1

        for i in 'abcdefghijklmnopqrstuvwxyz':
            result[i] = tuple(eng_alphabet[i])
        for i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
            result[i] = tuple(rus_alphabet[i])
        return result


# Перевод числа, состоящего из римских цифр, в целое число
# Необходимо разработать функцию roman_numerals_to_int(roman_numeral), которая выполнит
# перевод числа из римской нотации в десятичную целочисленную нотацию. Римское число
# задается в виде строки, возвращаемый результат должен иметь тип int, если трансляция прошла
# успешно, либо None, если возникли проблемы с переводом числа.
def roman_numerals_to_int(roman_numeral):
    result = 0
    r_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    try:
        for i in range(len(roman_numeral) - 1):
            if r_numerals[roman_numeral[i]] < r_numerals[roman_numeral[i + 1]]:
                result = result - r_numerals[roman_numeral[i]]
            else:
                result = result + r_numerals[roman_numeral[i]]
        result = result + r_numerals[roman_numeral[-1]]
        return result
    except:
        return None


if __name__ == "__main__":
    pass
