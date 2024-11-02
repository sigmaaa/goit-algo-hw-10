import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable(
    'Fruit_juice', lowBound=0, cat='Integer')

# Функція цілі (Максимізація прибутку)
model += lemonade + fruit_juice, "Total_Production"

# Додавання обмежень
model += 2*lemonade + 1*fruit_juice <= 100, "Water_Limit"
model += 1*lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Результати оптимізації:")
print(f"Кількість виробленого Лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість виробленої продукції: {model.objective.value()}")
