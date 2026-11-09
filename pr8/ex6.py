balance = 1000.0


def show_balance():
    print("[Баланс]: Поточний залишок:", round(balance, 2), "грн")


def deposit(amount):
    global balance
    if amount <= 0:
        print("[Помилка]: Сума поповнення має бути більшою за нуль!")
        return
    balance += amount
    print("[Успіх]: Рахунок поповнено на", round(amount, 2), "грн.")


def withdraw(amount):
    global balance
    if amount <= 0:
        print("[Помилка]: Сума зняття має бути більшою за нуль!")
        return
    if amount > balance:
        print("[Помилка]: Недостатньо коштів! Доступно:", round(balance, 2), "грн.")
        return
    balance -= amount
    print("[Успіх]: Знято", round(amount, 2), "грн.")


def run_banking_system():
    while True:
        print()
        print("===== БАНКІВСЬКИЙ РАХУНОК =====")
        print("1. Поповнити баланс")
        print("2. Зняти кошти")
        print("3. Переглянути баланс")
        print("0. Вихід")
        print()

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            try:
                val = float(input("Введіть суму для поповнення: "))
                deposit(val)
            except ValueError:
                print("[Помилка]: Введіть коректне числове значення.")
        elif choice == "2":
            try:
                val = float(input("Введіть суму для зняття: "))
                withdraw(val)
            except ValueError:
                print("[Помилка]: Введіть коректне числове значення.")
        elif choice == "3":
            show_balance()
        elif choice == "0":
            print("Дякуємо за користування сервісом! До побачення.")
            break
        else:
            print("[Помилка]: Невідома команда. Спробуйте ще раз.")


run_banking_system()