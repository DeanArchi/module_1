from functions import load_path, save_data, translate, compare_sums, lang_detect, validate_language, sum_of_squares, square_of_sum


def main():
    file_path = 'MyData.json'
    data = load_path(file_path)

    if data is None:
        numbers = input("Введіть два цілих числа: ").split()
        lang = input("Введіть мову інтерфейсу (uk/en): ").strip().lower()
        # перевірка, чи введено коректно мову
        lang = validate_language(lang)
        data = {"numbers": list(map(int, numbers)), "language": lang}
        save_data(file_path, data)
        print(f"Дані збережено в файл {file_path}")
        return

    # витягування з файлу код мови та два числа
    language = validate_language(data.get('language'))
    a, b = data['numbers']

    # обчислення суми квадратів та квадрат суми
    sum_squares = sum_of_squares(a, b)
    square_sum = square_of_sum(a, b)

    print(translate('Мова: ', language), lang_detect(language))
    print(translate('Два цілих числа: ', language), a, b, '\n')
    print(translate('Сума квадратів: ', language), f"{a}^2 + {b}^2 = {a ** 2} + {b ** 2} = {sum_squares}")
    print(translate('Квадрат суми: ', language), f"({a}+{b})^2 = {square_sum}")

    # порівняння суми квадратів та квадрату суми
    result = compare_sums(sum_squares, square_sum, language)
    print(result)


if __name__ == "__main__":
    main()
