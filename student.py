class Student:

    def __init__(self, name, year, vstup_year, grades):
        self.name = name
        self.year = year
        self.vstup_year = vstup_year
        self.grades = grades

    def __repr__(self):
        oc, ooi, db, tspp = self.grades
        return f'{self.name} - Рік народження: {self.year}, рік вступу: {self.vstup_year}, ОС: {oc}, ООІ: {ooi}, ДБ: {db}, ТСПП: {tspp}'

    @staticmethod
    def get_students(filepath):
        with open(filepath, 'r') as file:
            lines = file.read().splitlines()

            students = []

            for line in lines:
                info = line.split(' ', 3)
                grades = line.rsplit(' ', 4)
                info.pop()
                grades.pop(0)
                student = Student(*info, [int(grade) for grade in grades])
                students.append(student)

        return students