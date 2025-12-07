# class Book:
#     def __init__(self, title, author, year, pages):
#         self.title = title #название
#         self.author = author #автор
#         self.year = year #год
#         self.pages = pages #страница
#
#     def info(self):
#         print(f'название книги {self.title},',f'афтор книги {self.author},', f'создано в {self.year},', f'страница {self.pages}')
#
# book_one = Book('война и мир','Л.Т','1978','189')
# book_two = Book('крвсное яблоко','Ч.А','1997','120')
# book_free = Book('девять объезян','М.Р','1980','489')
# book_for = Book('белый пороход','Ч.А','1906','236')
#
# print(book_one.title , book_one.author , book_one.year , book_one.pages)
# print(book_two.title , book_two.author , book_two.year , book_two.pages)
# print(book_free.title , book_free.author , book_free.year , book_free.pages)
# print(book_for.title , book_for.author , book_for.year , book_for.pages)
#
# book_one.info()
# book_two.info()
# book_free.info()
# book_for.info()
# 3. Класс Student
#
# Создать файл students.py.
#
# Создать класс Student
#
# Атрибуты: name, age, course, grades (список оценок)
#
# Метод average_grade() возвращает средний балл
#
# Метод introduce() рассказывает о студенте
#
# Создать пару студентов и вывести их средние оценки.
#
# 4. Класс Animal
#
# Создать файл animals.py.
#
# Создать класс Animal
#
# Атрибуты: species, name, age
#
# Метод speak() выводит звук:
# Например: "Кот Барсик говорит: мяу!"
#
# Создать объекты разных животных.
#
# 5. Класс Movie
#
# Создать файл movies.py.
#
# Создать класс Movie
#
# Атрибуты: title, director, year, genre
#
# Метод describe() выводит описание фильма
#
# Создать 3 фильма и вывести их атрибуты.
#
# 6. Класс Employee
#
# Создать файл employee.py.
#
# Создать класс Employee
#
# Атрибуты: name, position, salary
#
# Метод info() выводит:
# "Имя: Анна, должность: менеджер, зарплата: 70000"
#
# Метод increase_salary(percent) увеличивает зарплату на заданный процент
#
# Создать несколько сотрудников и поднять одному зарплату.
#
# 7. Класс Country
#
# Создать файл countries.py.
#
# Создать класс Country
#
# Атрибуты: name, population, continent, capital
#
# Метод describe() выводит сводную информацию
#
# Создать 2–3 страны.#
# 3. Класс Student
#from pydoc import describe


#Создать файл students.py.

#  Создать класс Student
#
# Атрибуты: name, age, course, grades (список оценок)
#
# Метод average_grade() возвращает средний балл
#
# Метод introduce() рассказывает о студенте
# #
# Создать пару студентов и вывести их средние оценки.#
# class Student:
#     def __init__(self, name, age, course, grades):
#         self.name = name  # имя студента
#         self.age = age  # возраст
#         self.course = course  # курс обучения
#         self.grades = grades  # список оценок
#
#     def average_grade(self):
#         """Возвращает средний балл студента"""
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#
#     def introduce(self):
#         """Выводит информацию о студенте"""
#         print(f"Меня зовут {self.name}, мне {self.age} лет, "
#               f"я учусь на {self.course} курсе. "
#               f"Мой средний балл: {self.average_grade():.2f}")
#
#
# # Создание объектов студентов
# student_one = Student("Алибек", 18, 1, [5, 4, 5, 3, 4])
# student_two = Student("Айдана", 20, 2, [4, 4, 5, 5, 5])
#
# # Вывод средних оценок
# print("Средний балл студента 1:", student_one.average_grade())
# print("Средний балл студента 2:", student_two.average_grade())
#
# # Представление студентов
# student_one.introduce()

# student_two.introduce()
###Создайте несколько разных объектов (Classmate, Friend, Person).
# Поместите их все в один список. Затем напишите цикл, который проходит
# по этому списку и для каждого объекта вызывает метод introduce().№№
# class Person:
#     def __init__(self, name, birth_date, occupation, higher_education):
#         self.name = name
#         self.birth_date = birth_date
#         self.occupation = occupation
#         self.higher_education = higher_education
#
#     def introduce(self):
#         introduce = ("по професия я "
#                      if self.higher_education
#                      else "нет професии")
#         print(f"Меня зовут {self.name},", f"я родился {self.birth_date}", f"по профессии {self.occupation}",
#               f"{introduce}.")
#
#
# class Classmate(Person):
#     def __init__(self, name, birth_date, occupation, higher_education, group_name):
#         super().__init__(name, birth_date, occupation, higher_education)
#         self.group_name = group_name
#
#     def introduce(self):
#         """Дополнительная информация"""
#         print(f"Меня зовут {self.name}", f"я родился {self.birth_date}",
#               f"по профессии {self.occupation} , имею {self.higher_education},мой одногрупник  {self.group_name}")
#
#
# classmate_one = Classmate("Artur", "16.01.2008", "прошраммист", "среднее образование", "Алмаз")
# classmate_two = Classmate("Arslan", "23.04.2005", "врач", "высшее оброзование", "Алмаз")
# classmate_one.introduce()
# classmate_two.introduce()
#
#
# class Friend(Person):
#     def __init__(self, name, birth_date, occupation, higher_education, hobby, friend):
#         super().__init__(name, birth_date, occupation, higher_education)
#         self.hobby = hobby
#         self.friend = friend
#
#     def introduce(self):
#         """Дополнительная информация"""
#         print(f"Меня зовут {self.name},", f"я родился {self.birth_date}", f',я друг {self.friend}',
#               f"по профессии {self.occupation} , имею {self.higher_education},моё хобби {self.hobby}")
#
#
# friend_one = Friend("Бексултан", "27.09.2000", "хирург", "высшее образование", "бокс", "Алмаза")
# friend_two = Friend("Арген", "15.03.2007", "машинист", "среднее образование", "бег", "Алмаза")
# friend_one.introduce()
# friend_two.introduce()
#
# people = [classmate_one,classmate_two,friend_one,friend_two]
#
# for v in people:
#     v.introduce()
# 🔹 Задача 1. Животные и их особенности
#
# Создай класс Animal с атрибутами: name, age.
#
# Добавь метод describe(), который выводит информацию о животном.
#
# Создай два класса-наследника:
#
# Dog — добавь атрибут breed
#
# Cat — добавь атрибут color
#
# Переопредели метод describe() так, чтобы он выводил дополнительные данные.
#
# Создай по два объекта каждого класса и вызови метод describe().

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def describe(self):
        describi = f'введите имя животног'
        if self.name:
            print(f'имя животного {self.name}')
        else:
            print(f'нет таеого имени {self.name} ',f'{describi}' )

        if self.age:
            print(f'возраст животного {self.age}')
        else:
            print(f'нет такого возраста {self.age}',f'{describi}')

animal_one = Animal('Жираф','8')

animal_one.describe()
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def describe(self):
        print(f'gaf gaf {self.age}',f'my name {self.name}',f'я из породы {self.breed}')

dog_one =Dog('Шарик','4','немецкая авчарка')

dog_one.describe()

class Cat(Animal):
    def __init__(self, name ,age, color):
        super().__init__(name, age)
        self.color =color

    def describe(self):
        print(f'меня зовут {self.name}',f'мне {self.age} лет',f'цвет моей шерсти {self.color}')

cat_one =Cat('Муся','3','blak')
cat_two =Cat('Коржик','5','red')

cat_one.describe()
cat_two.describe()

class Gorilla(Animal):
    def __init__(self, name, age , weight):
        super().__init__( name, age)
        self.weight =weight

    def describe(self):
        print(f'моё имя {self.name} тебя не касается', f'мой возраст {self.age}',f'вес имею {self.weight}')

gorilla_one = Gorilla('Титан','23','350')
gorilla_two = Gorilla('Виктор','44','459')

gorilla_one.describe()
gorilla_two.describe()