import os
import json
from googletrans import Translator, LANGUAGES


def sum_of_squares(a, b):
    """
        Обчислює суму квадратів двох чисел
    """
    return a**2 + b**2


def square_of_sum(a, b):
    """
        Обчислює квадрат суми двох чисел
    """
    return (a + b) ** 2


def compare_sums(sum_squares, square_sum, lang):
    """
        Порівнює значення суми квадратів та квадрату суми
    """
    if sum_squares > square_sum:
        return translate('Сума квадратів більше!', lang)
    if sum_squares < square_sum:
        return translate('Квадрат суми більше!', lang)
    return translate('Суми рівні', lang)


def lang_detect(lang):
    """
        Визначає мову у текстовому вигляді (Українська, English і тд.)
    """
    language = LANGUAGES[lang]
    return translate(language.capitalize(), lang)


def validate_language(lang):
    """
        Перевіряє чи введена мова є коректною, якщо ні, використовує 'uk'.
    """
    if lang in LANGUAGES:
        return lang
    else:
        print("Некоректна мова, буде використано українську.")
        return 'uk'


def translate(text, language):
    """
        Перекладає текст
    """
    try:
        translator = Translator()
        translation = translator.translate(text, language)
        return translation.text
    except Exception as e:
        return f"Error: {e}"


def load_path(file_path):
    """
        Читання файлу
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Некоректні дані в файлі.")
    return None


def save_data(file_path, data):
    """
        Збереження у файл
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)
