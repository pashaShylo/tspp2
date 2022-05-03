from student import Student

def get_result(students):
    result = []

    for student in students:
        flag = False
        for i in student.grades:
            if i == 2:
                flag = True
                break
        if flag:
            result.append(student)

    return result

students = Student.get_students('students.txt')

result = get_result(students)

for i in result:
    print(i)