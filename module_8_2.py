def personal_sum(numbers: list) -> tuple:
    result, incorrect_data = 0, 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'некорректный тип данных для подсчета суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers: list) -> int | float | None:
    try:
        s, incorrect_data = personal_sum(numbers)
        return s / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
