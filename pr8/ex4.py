def analyze_grades(*grades):
    if not grades:
        return {
            "average": 0.0,
            "max": None,
            "min": None,
            "passed": 0
        }

    avg = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed_count = sum(1 for grade in grades if grade >= 60)

    return {
        "average": round(avg, 2),
        "max": highest,
        "min": lowest,
        "passed": passed_count
    }


result = analyze_grades(95, 78, 60, 88, 45, 100)
print("Результати:", result)

empty_result = analyze_grades()
print("Без аргументів:", empty_result)