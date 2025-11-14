// Массив студентов
var groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БВТ1702",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1702",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БАП1801",
        "marks": [5, 5, 5]
    }
];

// Функция для форматирования строки
var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

// Функция вывода списка студентов
var printStudents = function(students){
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i < students.length; i++){
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'].join(', '), 20)
        );
    }
    console.log('\n');
};

// Выводим список
printStudents(groupmates);

// Функция фильтрации по группе
function filterByGroup(groupName) {
    var filtered = groupmates.filter(function(student) {
        return student.group === groupName;
    });
    console.log("Студенты группы " + groupName + ":");
    printStudents(filtered);
}

// Функция фильтрации по средней оценке
function filterByAverageGrade(minAverage) {
    var filtered = groupmates.filter(function(student) {
        var average = student.marks.reduce((a, b) => a + b, 0) / student.marks.length;
        return average > minAverage;
    });
    console.log("Студенты со средним баллом выше " + minAverage + ":");
    printStudents(filtered);
}

// Пример использования:
// filterByGroup("БВТ1702");
// filterByAverageGrade(4.5);