from student import Student

def get_result(students):
    result = []
    for student in students:
        flag = True

        if student.grades.count(4) == 1:
            for grade in student.grades:
                if grade < 4:
                    flag = False
                    break
        else:
            flag = False

        if flag:
            result.append(student)

    return result

students = Student.get_students('students.txt')

result = get_result(students)

for i in result:
    print(i)