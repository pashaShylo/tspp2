from student import Student

def get_result(students):
    result = []
    for student in students:
        flag = 0
        for grade in student.grades:
            if (grade == 3):
                flag += 1
        if (flag == 1):
            result.append(student)

    return result

students = Student.get_students('students.txt')

result = get_result(students)

for i in result:
    print(i)