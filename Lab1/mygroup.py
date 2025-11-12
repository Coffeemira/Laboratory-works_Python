groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10),
              str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def filter_by_average(students, threshold):
    filtered = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > threshold:
            filtered.append(student)
    return filtered

# --- Основной код ---
print("Все студенты:")
print_students(groupmates)

print("\nСтуденты со средним баллом выше 4.0:")
threshold = float(input("Введите порог среднего балла: "))
filtered_students = filter_by_average(groupmates, threshold)
print_students(filtered_students)