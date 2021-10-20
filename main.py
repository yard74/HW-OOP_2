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
