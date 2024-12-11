class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = None

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def give_lecture_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hm(self):
        grades = self.grades.values()
        all_marks = []
        for grade in grades:
                for mark in grade:
                    all_marks.append(mark)
        self.average = round(sum(all_marks) / len(all_marks), 1)
        return self.average

    def __str__(self):
        return (f'Имя: {self.name} '
                f'\nФамилия: {self.surname} '
                f'\nСредняя оценка за домашние задания: {self.average} '
                f'\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {', '.join(self.finished_courses)}')

    def __gt__(self, Student):
        return self.average > Student.average

    def __lt__(self, Student):
        return self.average < Student.average

    def __ge__(self, Student):
        return self.average >= Student.average

    def __le__(self, Student):
        return self.average <= Student.average

    def __eq__(self, Student):
        return self.average == Student.average

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = None

    def average_grade(self):
        grades = self.grades.values()
        all_marks = []
        for grade in grades:
                for mark in grade:
                    all_marks.append(mark)
        self.average = round(sum(all_marks) / len(all_marks), 1)
        return self.average

    def __gt__(self, Lecturer):
        return self.average > Lecturer.average

    def __lt__(self, Lecturer):
        return self.average < Lecturer.average

    def __ge__(self, Lecturer):
        return self.average >= Lecturer.average

    def __le__(self, Lecturer):
        return self.average <= Lecturer.average

    def __eq__(self, Lecturer):
        return self.average == Lecturer.average

    def __str__(self):
        return (f'Имя: {self.name} '
                f'\nФамилия: {self.surname} '
                f'\nСредняя оценка за лекции: {self.average}')

class Reviewer (Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} '
                f'\nФамилия: {self.surname}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']



cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)

best_student.average_hm()


best_student1 = Student('Ruoy1', 'Eman1', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Git']


cool_mentor.rate_hw(best_student1, 'Python', 10)
cool_mentor.rate_hw(best_student1, 'Python', 10)
cool_mentor.rate_hw(best_student1, 'Python', 8)
cool_mentor.rate_hw(best_student1, 'Git', 8)

best_student1.average_hm()

print(best_student1.average)

print(best_student.__le__(best_student1))
