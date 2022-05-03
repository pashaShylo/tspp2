from student import Student

def get_result(students):
    result = []
    for student in students:
        flag = True

        for i in student.grades:
            if i < 5:
                flag = False
                break

        if flag:
            result.append(student)

    return result

students = Student.get_students('students.txt')

result = get_result(students)

for i in result:
    print(i)