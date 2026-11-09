def calculate(a, b, operation="+"):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Помилка: ділення на нуль неможливе!"
        return a / b
    elif operation == "**":
        return a ** b
    else:
        return "Помилка: невідома операція '" + str(operation) + "'"


print("Додавання:", calculate(10, 5))
print("Віднімання:", calculate(10, 5, "-"))
print("Множення:", calculate(10, 5, "*"))
print("Ділення:", calculate(10, 5, "/"))
print("Ділення на нуль:", calculate(10, 0, "/"))
print("Степінь:", calculate(2, 4, "**"))
print("Невідома операція:", calculate(10, 5, "%"))