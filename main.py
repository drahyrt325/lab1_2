def gcd_euclidean(a: int, b: int) -> int:
    """
    Алгоритм Евклида для нахождения НОД двух чисел.

    Args:
        a: первое целое число
        b: второе целое число

    Returns:
        Наибольший общий делитель чисел a и b
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def main():
    """Основная функция программы."""
    print("Нахождение НОД двух чисел с помощью алгоритма Евклида")
    print("=" * 50)

    try:
        # Ввод чисел от пользователя
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        # Вычисление НОД
        result = gcd_euclidean(num1, num2)

        # Вывод результата
        print(f"\nНОД чисел {num1} и {num2} равен: {result}")

        # Дополнительная информация
        if result == 1:
            print("Числа являются взаимно простыми.")

    except ValueError:
        print("Ошибка: пожалуйста, введите целые числа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()