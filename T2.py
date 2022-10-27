money_capital = 10000  # финансовая подушка безопасности!!!
salary = 5000          # ежемесячная зарплата!!! приток
spend = 6000          # расходы на проживание
increase = 0.05      # ежемесячный рост цен

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
while money_capital + salary > spend:
    if money_capital > spend:
        money_capital -= spend
        month += 1
        spend = spend + spend * increase
        money_capital = money_capital + salary - spend
        if money_capital > 0:
            month += 1
            spend = spend + spend * increase
            money_capital += salary
    elif money_capital < spend:
        money_capital = money_capital + salary - spend
        month += 1


print(month)