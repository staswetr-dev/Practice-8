def check_password(password):
    errors = []

    if len(password) < 8:
        errors.append("довжина менше 8 символів")
    if not any(char.isdigit() for char in password):
        errors.append("відсутня хоча б одна цифра")
    if not any(char.isupper() for char in password):
        errors.append("відсутня хоча б одна велика літера")

    if not errors:
        return "Надійний пароль"
    return "Слабкий пароль (причини: " + ", ".join(errors) + ")"


passwords_to_test = ["Python123", "hello", "OnlyLetters", "12345678", "Pass1"]
for pwd in passwords_to_test:
    print(pwd, "->", check_password(pwd))