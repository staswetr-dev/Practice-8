def create_profile(name, age, **kwargs):
    profile = {
        "name": name,
        "age": age
    }
    profile.update(kwargs)
    return profile


def print_profile(profile):
    print("----- ПРОФІЛЬ КОРИСТУВАЧА -----")
    for key, value in profile.items():
        print(" ", key.capitalize() + ":", value)
    print("-------------------------------")


def update_profile(profile, **kwargs):
    profile.update(kwargs)
    return profile


p1 = create_profile(
    "Олександр", 19,
    city="Дніпро",
    group="КН-24",
    specialty="Computer Science",
    email="student@example.com"
)

p2 = create_profile(
    "Марія", 20,
    city="Київ",
    faculty="ФІОТ",
    is_active=True
)

p3 = create_profile(
    "Богдан", 22,
    city="Львів",
    phone="+380991112233"
)

print_profile(p1)
print_profile(p2)
print_profile(p3)

update_profile(p1, city="Варшава", semester=4)
print_profile(p1)