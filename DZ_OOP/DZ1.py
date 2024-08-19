def average_grade(grades):
        if not grades:
            return 0 

        grades_count = 0  
        total_grade = 0 

        for _, grades_list in grades.items():
            grades_count += len(grades_list)  
            total_grade += sum(grades_list) 

        average_g = round(total_grade / grades_count, 2)

        return average_g 



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
        

   
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {average_grade(self.grades)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")  
     
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]     
            print(lecturer.grades)
            return
        else:
            print('Ошибка')
            return 

    def __lt__(self, other):
        if not isinstance(other, type(self)) or type(average_grade(self.grades)) != float or type(average_grade(other.grades)) != float:
                return "It's wrong!"
        return average_grade(self.grades) < average_grade(other.grades)
             
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
   

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        


        
        
    def rate_hw(self, student, course, grade):
           if isinstance(student, Student) and course in self.courses_attached and (course in student.courses_in_progress or course in student.finished_courses):
               if course in student.grades:
                   student.grades[course] += [grade]
               else:
                student.grades[course] = [grade]
           else:
                return 'Ошибка'
    
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')      

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}') 

    def __lt__(self, other):
        if not isinstance(other, type(self)) or type(average_grade(self.grades)) != float or type(average_grade(other.grades)) != float:
            return "It's wrong!"
        return average_grade(self.grades) < average_grade(other.grades)  







# Lecturer 1
lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Основы']
# Lecturer 2
lecturer_2 = Lecturer('Алена', 'Батицкая')
lecturer_2.courses_attached += ['Git']
# Lecturer 3
lecturer_3 = Lecturer('Тимур', 'Анвартдинов')
lecturer_3.courses_attached += ['ООП']

student_1 = Student('Билл', 'Гейтс', 'мужской')
student_1.rate_lect(lecturer_1, 'Основы', 8 )
student_1.rate_lect(lecturer_2, 'Git', 7)
student_1.rate_lect(lecturer_3, 'ООП', 9)
student_1.courses_in_progress += ['ООП']
student_1.finished_courses += ['Основы']
student_1.finished_courses += ['Git']
# Student 2
student_2 = Student('Марк', 'Цукерберг', 'мужской')
student_2.rate_lect(lecturer_1, 'Основы', 10)
student_2.rate_lect(lecturer_2,'Git', 8)
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Основы']
# Student 3
student_3 = Student ('Дональд', 'Эрвин', 'мужской')
student_3.rate_lect(lecturer_1, ['Основы'], 4)
student_3.courses_in_progress += ['Основы']
student_3.finished_courses += ['нет завершенных курсов']







# Student 1
reviewer = Reviewer('Билл', 'Гейтс')
reviewer.courses_attached = ['Основы', 'Git', 'ООП']
reviewer.rate_hw(student_1, 'ООП', 8)
reviewer.rate_hw(student_1, 'Git', 9)
reviewer.rate_hw(student_1, 'Основы', 6)
reviewer.rate_hw(student_2, 'Git', 9)
reviewer.rate_hw(student_2, 'Основы', 8)
reviewer.rate_hw(student_3, 'Основы', 7)

print(student_1)
print(student_2)
print(student_3)
print(lecturer_1)
print(lecturer_2)
print(lecturer_3)



print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()


print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()

