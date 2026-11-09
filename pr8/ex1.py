def calculate_total(price, quantity):
    return price * quantity


purchases = [
    (250, 3),
    (12.50, 10),
    (499.99, 2)
]

for price, qty in purchases:
    total = calculate_total(price, qty)
    print("Ціна:", price, "грн | Кількість:", qty, "| Загальна вартість:", round(total, 2), "грн")