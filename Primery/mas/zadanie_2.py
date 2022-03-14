# 1. Создать следующую иерархию классов: человек (Person), студент (Student), служащий (Employee). 
# Один из этих классов является родительским, остальные два – дочерними. Определить самим. 
# Человек имеет следующие данные: имя, фамилия, возраст. У класса, реализующего этот тип, должен быть метод, который выводить данные на экран. 
# Переменные класса «студент»: ВУЗ, факультет, курс. Класс также имеет метод для вывода данных. 
# Класс «служащий». Данные: место работы (компания), должность. Имеется метод для вывода данных. 
# 2. Придумать самим иерархию классов. Реализовать и привести пример использования.

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def person_print(self):
        print("Имя ", self.name)
        print("Фамилия ", self.surname)
        print("Возрост ", self.age)

class Student(Person):

    def __init__(self, name, surname, age, university, faculty, course):
        Person.__init__(self, name, surname, age)
        self.university = university
        self.faculty = faculty
        self.course = course

    def student_print(self):
        self.person_print()
        print("Университет ", self.university)
        print("Факультет ", self.faculty)
        print("Курс ", self.course)


class Employee(Person):
    def __init__(self, name, surname, age, place_of_work, post):
        Person.__init__(self, name, surname, age)
        self.place_of_work = place_of_work
        self.post = post
    
    def employee_print(self):
        self.person_print()
        print("Место работы ", self.place_of_work)
        print("Должность ", self.post)

# person_11 = Person("Имя", "Фамилия", "22")
# person_1 = Employee("МУК", "Инженео")
# person_1.employee_print()
Student1 = Student('Alisher','Nurasdf', 42,'Iuk', 'ISIT', 5)
Student1.student_print()
print("------------------------------")
student12 = Employee('Ali','Nu', 5, "Мук", "Инженер")
student12.employee_print()