# cart_service.py
# Модуль: CartModule (Корзина)
# User Story: Как студент, я хочу добавлять блюда в корзину и применять промокод для скидки.

class CartModule:
    def __init__(self):
        # Заглушка (Stub) для связи с внешним модулем скидок
        self.external_discount_service = "Active"

    def calculate_total(self, items_prices, promo_code=None):
        """
        Рассчитывает итоговую сумму корзины.
        :param items_prices: список цен (числа)
        :param promo_code: строка промокода (опционально)
        :return: float - итоговая сумма
        """
        # Проверка на пустую корзину или некорректные данные
        if not items_prices or not isinstance(items_prices, list):
            return 0.0

        # Базовый расчет суммы
        total = sum(items_prices)

        # Логика применения промокода
        if promo_code == "STUDENT2024":
            total = total * 0.9  # Скидка 10%
        
        # Защита от отрицательной суммы
        return max(0.0, total)
