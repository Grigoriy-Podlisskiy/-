salary = 5000  # зарплата
spend = 6000   # расходы
months = 10    # количество месяцев
increase = 0.03    # ежемесячный рост цен

def survival(salary, spend, months, increase):

    max_salary = 0      # количество заработанных денег за months (10) месяцев
    max_spend_inc = 0   # сумма расходов за months (10) месяцев с учетом ежемесячного роста цен

    for _ in range(1, months +1):
        max_salary += salary                # считаем количество заработанных денег за months (10) месяцев
        max_spend_inc += spend                  # для первой итерации расходы без увеличения (условие задачи)
        spend = spend + spend * increase    # расходы повышаются со второго месяца ежемесячно на 3%

    need_money = max_spend_inc - max_salary  # необходимая сумма денег, чтобы прожить 10 месяцев
    return round(need_money)

print(survival(5000, 6000, 10, 0.03))