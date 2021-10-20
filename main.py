class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 < grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print(f'Неправильная оценка для {lecturer.surname} {lecturer.name} по курсу {course}.')
        else:
            return 'Ошибка'

    def stud_avg_hw_grade(self):
        sum_grades = 0
        i = 0
        for course in self.courses_in_progress:
            for grade in self.grades[course]:
                sum_grades += grade
                i += 1
        res = (sum_grades / i)
        return round(res, 2)

    def __str__(self):
        student_info = f'Имя: {self.name}\nФамилия: {self.surname}\n'\
                       f'Средняя оценка за домашние задания: {self.stud_avg_hw_grade()}\n'\
                       f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
                       f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return student_info

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Кто то не является Студентом!')
            return
        return self.stud_avg_hw_grade() < other.stud_avg_hw_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Кто то не является Студентом!')
            return
        return self.stud_avg_hw_grade() > other.stud_avg_hw_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Кто то не является Студентом!')
            return
        return self.stud_avg_hw_grade() <= other.stud_avg_hw_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            print('Кто то не является Студентом!')
            return
        return self.stud_avg_hw_grade() >= other.stud_avg_hw_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Кто то не является Студентом!')
            return
        return self.stud_avg_hw_grade() == other.stud_avg_hw_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            print('Кто то не является Студентом!')
            return
        return self.stud_avg_hw_grade() != other.stud_avg_hw_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lec_avg_grade(self):
        sum_grades = 0
        i = 0
        for course in self.courses_attached:
            for grade in self.grades[course]:
                sum_grades += grade
                i += 1
        res = (sum_grades / i)
        return round(res, 2)

    def __str__(self):
        lecturer_info = f'Имя: {self.name}\nФамилия: {self.surname}\n'\
                        f'Средняя оценка за лекции: {self.lec_avg_grade()}'
        return lecturer_info

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Кто то не является Лектором!')
            return
        return self.lec_avg_grade() < other.lec_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Кто то не является Лектором!')
            return
        return self.lec_avg_grade() > other.lec_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Кто то не является Лектором!')
            return
        return self.lec_avg_grade() <= other.lec_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print('Кто то не является Лектором!')
            return
        return self.lec_avg_grade() >= other.lec_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Кто то не является Лектором!')
            return
        return self.lec_avg_grade() == other.lec_avg_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            print('Кто то не является Лектором!')
            return
        return self.lec_avg_grade() != other.lec_avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_info = f'Имя: {self.name}\nФамилия: {self.surname}'
        return reviewer_info


best_student = Student('Петя', 'Васечкин', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['English for programmers']

worst_student = Student('Ваня', 'Двоечкин', 'male')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['GIT']

student_list = [best_student, worst_student]

cool_lecturer = Lecturer('Анна', 'Васильева')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']

worst_lecturer = Lecturer('Наталья', 'Кукушкина')
worst_lecturer.courses_attached += ['Python']
worst_lecturer.courses_attached += ['GIT']

lecturer_list = [cool_lecturer, worst_lecturer]

cool_reviewer = Reviewer('Иван', 'Иванов')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

best_reviewer = Reviewer('Илья', 'Соболев')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['GIT']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'GIT', 10)

best_reviewer.rate_hw(worst_student, 'Python', 6)
best_reviewer.rate_hw(worst_student, 'GIT', 2)
best_reviewer.rate_hw(worst_student, 'GIT', 4)

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'GIT', 9)
best_student.rate_lecture(cool_lecturer, 'GIT', 8)
best_student.rate_lecture(cool_lecturer, 'GIT', 9)

worst_student.rate_lecture(worst_lecturer, 'Python', 10)
worst_student.rate_lecture(worst_lecturer, 'Python', 8)
worst_student.rate_lecture(worst_lecturer, 'GIT', 9)
worst_student.rate_lecture(worst_lecturer, 'GIT', 7)
worst_student.rate_lecture(worst_lecturer, 'GIT', 5)


def get_avg_hw_grade_in_course(stud_list, course):
    sum_grades = 0
    count_grades = 0
    for student in stud_list:
        sum_grades += sum(student.grades[course])
        count_grades += len(student.grades[course])
    return print(round((sum_grades / count_grades), 2))


def get_avg_lecture_grade_in_course(lec_list, course):
    sum_grades = 0
    count_grades = 0
    for lecturer in lec_list:
        sum_grades += sum(lecturer.grades[course])
        count_grades += len(lecturer.grades[course])
    return print(round((sum_grades / count_grades), 2))


print(f'Проверка принта Ревьюэра:\n{cool_reviewer}')
print()
print(f'Проверка принта Лектора:\n{cool_lecturer}')
print()
print(f'Проверка принта Студента:\n{best_student}')
print()
print(f'Проверка сравнения студентов:\n{best_student <= worst_student}')
print()
print(f'Проверка сравнения лекторов:\n{cool_lecturer > worst_lecturer}')
print()
print('Проверка работы функции расчета средней оценки за ДЗ всех студентов в рамках курса GIT:')
get_avg_hw_grade_in_course(student_list, 'GIT')
print()
print('Проверка работы функции расчета средней оценки за лекции всех лекторов в рамках курса GIT:')
get_avg_hw_grade_in_course(lecturer_list, 'GIT')