# test_cart.py
# Тестовый драйвер для CartModule

from cart_service import CartModule

def run_tests():
    cart = CartModule()
    
    print("=" * 50)
    print("ЗАПУСК ТЕСТОВ CartModule (FoodCampus)")
    print("=" * 50)

    # === ПОЗИТИВНЫЕ ТЕСТЫ (Happy Path) ===
    print("\n--- Позитивные тесты ---")

    # Тест 1: Обычный расчет
    res1 = cart.calculate_total([100, 200, 50])
    print(f"Тест 1 - Обычный расчет [100, 200, 50]:")
    print(f"  Ожидается: 350.0 | Получено: {res1}")
    assert res1 == 350.0, f"FAIL! Получено {res1}"
    print("  ✅ PASS")

    # Тест 2: Применение промокода
    res2 = cart.calculate_total([1000], "STUDENT2024")
    print(f"\nТест 2 - Промокод STUDENT2024 [1000]:")
    print(f"  Ожидается: 900.0 | Получено: {res2}")
    assert res2 == 900.0, f"FAIL! Получено {res2}"
    print("  ✅ PASS")

    # Тест 3: Пустая корзина
    res3 = cart.calculate_total([])
    print(f"\nТест 3 - Пустая корзина []:")
    print(f"  Ожидается: 0.0 | Получено: {res3}")
    assert res3 == 0.0, f"FAIL! Получено {res3}"
    print("  ✅ PASS")

    # Тест 4: Неверный промокод
    res4 = cart.calculate_total([100], "INVALID")
    print(f"\nТест 4 - Неверный промокод [100], 'INVALID':")
    print(f"  Ожидается: 100.0 | Получено: {res4}")
    assert res4 == 100.0, f"FAIL! Получено {res4}"
    print("  ✅ PASS")

    # === НЕГАТИВНЫЕ ТЕСТЫ (Стресс-тесты) ===
    print("\n--- Негативные тесты (поиск багов) ---")

    # Тест 5: Отрицательная цена
    try:
        res5 = cart.calculate_total([-500, 100])
        print(f"\nТест 5 - Отрицательная цена [-500, 100]:")
        print(f"  Получено: {res5}")
        print(f"  ⚠️  БАГ: Программа приняла отрицательную цену! Сумма = {res5}")
    except Exception as e:
        print(f"\nТест 5 вызвал ошибку: {e}")

    # Тест 6: Текст вместо числа
    try:
        res6 = cart.calculate_total(["abc", 100])
        print(f"\nТест 6 - Текст в ценах ['abc', 100]:")
        print(f"  Получено: {res6}")
    except TypeError as e:
        print(f"\nТест 6 - Текст в ценах ['abc', 100]:")
        print(f"  ⚠️  БАГ: Программа упала с TypeError: {e}")

    # Тест 7: None вместо списка
    try:
        res7 = cart.calculate_total(None)
        print(f"\nТест 7 - None вместо списка:")
        print(f"  Получено: {res7}")
    except Exception as e:
        print(f"\nТест 7 - None вместо списка:")
        print(f"  ⚠️  БАГ: Программа упала: {e}")

    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 50)

if __name__ == "__main__":
    run_tests()
