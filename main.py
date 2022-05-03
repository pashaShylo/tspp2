from student import Student

def get_result(students):
    result = []
    for student in students:
        flag = True
        for grade in student.grades:
            if (grade != 5):
                flag = False
        if (flag):
            result.append(student)

    return result

students = Student.get_students('students.txt')

result = get_result(students)

for i in result:
    print(i)