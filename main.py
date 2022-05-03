from student import Student

def get_result(students):
    result = []
    for student in students:
        flag = False
        flag2 = False
        flag3 = True
        for grade in student.grades:
            if (grade == 5):
                flag = True
            if (grade == 4):
                flag2 = True
            if (grade <= 3):
                flag3 = False
        if (flag & flag2 & flag3):
            result.append(student)

    return result

students = Student.get_students('students.txt')

result = get_result(students)

for i in result:
    print(i)