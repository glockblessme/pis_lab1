groupmates = [
    {
        "name": "Павел",
        "surname": "Шипилов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Григорий",
        "surname": "Мурачёв",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Семён",
        "surname": "Вдовин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
        {
        "name": "Алексей",
        "surname": "Сивоконь",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Абрамов",
        "surname": "Григорий",
        "exams": ["История", "АиГ", "ЭЭиС"],
        "marks": [4, 4, 4]
    }
    
]

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(10), "Оценки")
    for s in students:
        print(s["name"].ljust(15), s["surname"].ljust(10), str(s["marks"]))

def filter_students_by_avg(students, min_avg):
    result = []
    for s in students:
        marks = s.get("marks", [])
        if marks:
            avg = sum(marks) / len(marks)
            if avg > min_avg:
                result.append(s)
    return result

def run_filter_and_print(students):
    raw = input("Введите минимальный средний балл: ").strip().replace(",", ".")
    try:
        min_avg = float(raw)
    except ValueError:
        print("Ошибка ввода: требуется число")
        return

    filtered = filter_students_by_avg(students, min_avg)
    if filtered:
        print_students(filtered)
    else:
        print(f"Студентов со средним баллом выше {min_avg} не найдено.")

run_filter_and_print(groupmates)


