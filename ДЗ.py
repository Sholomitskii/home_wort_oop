class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        a = []
        for el in self.grades.values():
            a += el
        aver_rate =  sum(a)/len(a)
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {aver_rate}\nКурсы в процессе обучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return output
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        a = []
        for el in self.grades.values():
            a += el
        aver_rate =  sum(a)/len(a)
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {aver_rate}'
        return output  

class Reviewer(Mentor):
    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Anton', 'Sholomitskii', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

notbest_student = Student('Petr', 'Vilkin', 'male')
notbest_student.courses_in_progress += ['Python']
notbest_student.courses_in_progress += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

psov_mentor = Reviewer('Gennadii', 'Psov')
psov_mentor.courses_attached += ['Python']

favorite_lecturer = Lecturer('Aristarh','Verevkin')
favorite_lecturer.courses_attached += ['Python']

gannibal_lecturer = Lecturer('Gannibal','Lecter')
gannibal_lecturer.courses_attached += ['Python']

stud_list_1 = [best_student, notbest_student]
def st_average_rating(stud_list, course):
    a = []
    for el in stud_list:
        if course in el.courses_in_progress:
            for k in el.grades[course]:
                a.append(k)
        else:
            print('Такой курс не изучали')
    print(sum(a)/len(a))

lect_list_1 = [favorite_lecturer, gannibal_lecturer]
def lec_average_rating(lect_list, course):
    a = []
    for el in lect_list:
        if course in el.courses_attached:
            for k in el.grades[course]:
                a.append(k)
        else:
            print('Такой курс не преподавали')
    print(sum(a)/len(a))

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)

cool_mentor.rate_hw(notbest_student, 'Python', 5)
cool_mentor.rate_hw(notbest_student, 'Git', 1)
cool_mentor.rate_hw(notbest_student, 'Python', 7)

best_student.rate_lecturer(favorite_lecturer, 'Python', 10)
notbest_student.rate_lecturer(favorite_lecturer, 'Python', 8)
best_student.rate_lecturer(gannibal_lecturer, 'Python', 9)
notbest_student.rate_lecturer(gannibal_lecturer, 'Python', 6)

print(best_student.grades) 
print(favorite_lecturer.grades)

print(best_student)
print(cool_mentor)
print(favorite_lecturer)

st_average_rating(stud_list_1 , 'Python')
st_average_rating(stud_list_1 , 'Git')

lec_average_rating(lect_list_1 , 'Python')
