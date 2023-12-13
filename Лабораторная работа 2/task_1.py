def calculate_months_to_empty_savings(money_capital, salary, spend, increase):
    months = 0

    while money_capital >= 0:
        # Рассчитываем бюджет текущего месяца
        monthly_budget = salary + money_capital

        # Проверяем, достаточно ли средств на текущем месяце
        if monthly_budget < spend:
            break  # Прерываем цикл, если средств недостаточно

        # Уменьшаем финансовую подушку безопасности
        money_capital -= spend

        # Увеличиваем расходы на следующем месяце
        spend *= (1 + increase / 100)

        # Увеличиваем количество пройденных месяцев
        months += 1

    return months
# Тест
money_capital = 100000  # Начальная финансовая подушка безопасности
salary = 50000  # Ежемесячная зарплата
spend = 30000  # Расходы на проживание
increase = 5  # Увеличение расходов ежемесячно на 5%

result = calculate_months_to_empty_savings(money_capital, salary, spend, increase)
print(f"Можно протянуть {result} месяцев без долгов.")
# Для этой задачи подойдет обычный цикл while