def calculate_required_savings(salary, spend, increase, target_months):
    money_capital = 0  # Начальная финансовая подушка безопасности
    months = 0

# В данном случае подойдет цикл с условием для выхода
    while months < target_months:
        # Рассчитываем бюджет текущего месяца
        monthly_budget = salary + money_capital

        if monthly_budget < spend:
            # Не хватает средств, увеличиваем подушку безопасности
            money_capital += spend - monthly_budget

        # Увеличиваем расходы на следующем месяце
        spend *= (1 + increase / 100)

        # Увеличиваем количество пройденных месяцев
        months += 1

    return round(money_capital, 2)

salary = 50000  # Ежемесячная зарплата
spend = 30000  # Расходы на проживание
increase = 3  # Увеличение расходов ежемесячно на 3%
target_months = 18 # Целевое количество месяцев без долгов

# Вычисляем необходимую подушку безопасности
required_savings = calculate_required_savings(salary, spend, increase, target_months)

print(f"Для протяжения {target_months} месяцев без долгов нужно иметь подушку безопасности: {required_savings} руб.")
