# from abc import ABC , abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def interesting(self):
#         pass
# class Cat(Animal):
#     def interesting(self):
#         print('мяу мяу мяуууу')
#
# class Dog(Animal):
#     def interesting(self):
#         print('гав гавг аааав')
#
# cat_one = Cat()
# dog_one = Dog()
# cat_one.interesting()
# dog_one.interesting()
# Homework 4





# Создай два класса: **`Contact`** и **`ContactList`**.
#
# ### 1. Класс Contact
#
# Этот класс будет описывать один контакт. У него должны быть **атрибуты**:
#
# - `name` - имя контакта
# - `phone_number` - номер телефона
#
# Также в этом классе нужно создать **статический метод** `validate_phone_number(phone_number)`, который проверяет, что телефонный номер содержит **ровно 10 цифр**. Если номер корректный, метод должен возвращать `True`, иначе - `False`.
#
# ### 2. Класс ContactList
#
# Этот класс будет отвечать за хранение всех контактов. В нём нужно:
#
# - создать **переменную класса** `all_contacts = []` - это список, в котором будут храниться все созданные объекты `Contact`.
# - создать **метод класса** `add_contact(name, phone_number)`,
#
#     который должен:
#
#     1. Проверить номер телефона с помощью `Contact.validate_phone_number(phone_number)`
#     2. Если номер правильный - создать новый объект `Contact` иначе вызвать ошибку
#     3. Добавить этот новый объект в список `all_contacts`.
# class Contact:
#     def __init__(self,name,phone_number):
#         self.name = name
#         self.phone_number = phone_number
#
#     @staticmethod
#     def validate_phone_number(self,phone_number):
#         if len(phone_number) != 10:
#             return False
#
#         for number in phone_number:
#             if number < '0' or number > '9':
#                 return False
#         return True
#
#
#
#
#
# class Dog:
#     color = 'red'
#     circle = '1'
### Ветка: hw6_1
#
# Классы:
#
# Player — базовый класс (play())
#
# AudioPlayer — наследуется от Player
#
# VideoPlayer — наследуется от Player
#
# SmartPlayer — наследуется от AudioPlayer и VideoPlayer
#
# Требование:
#
# Реализовать play() во всех классах так, чтобы
#
# SmartPlayer().play()
#
#
# выводил:
#
# SmartPlayer play
# AudioPlayer play
# VideoPlayer play
# Player play
#
# Задача 2. Система уведомлений
#
# Ветка: hw6_2
#
# Классы:
#
# Notifier — (send())
#
# EmailNotifier — наследуется от Notifier
#
# SMSNotifier — наследуется от Notifier
#
# MultiNotifier — наследуется от EmailNotifier и SMSNotifier
#
# Требование:
#
# Вызов:
#
# MultiNotifier().send()
#
#
# должен пройти по MRO и вывести сообщения каждого класса.
#
# Задача 3. Персонажи игры
#
# Ветка: hw6_3
#
# Классы:
#
# Character — (attack())
#
# Warrior — наследуется от Character
#
# Mage — наследуется от Character
#
# Paladin — наследуется от Warrior и Mage
#
# Требование:
# Paladin().attack()
#
#
# вызывает attack() в каждом классе через super().
#
# Задача 4. Логирование
#
# Ветка: hw6_4
#
# Классы:
#
# Logger — (log())
#
# FileLogger — наследуется от Logger
#
# ConsoleLogger — наследуется от Logger
#
# AppLogger — наследуется от FileLogger и ConsoleLogger
#
# Требование:
#
# Метод log() должен выводить информацию о порядке вызовов по MRO.
#
# Задача 5. Транспорт
#
# Ветка: hw6_5
#
# Классы:
#
# Transport — (move())
#
# LandTransport — наследуется от Transport
#
# WaterTransport — наследуется от Transport
#
# Amphibian — наследуется от LandTransport и WaterTransport
#
# Требование:
# Amphibian().move()
#
#
# вызывает move() всех классов по MRO.
#
# 💡 Общая подсказка для всех задач:
# print(ClassName.mro())
#
#
# Если хочешь, могу:
#
# дать правильные реализации,
#
# или намеренно сломанные варианты для отладки,
#
# или сделать один файл с автотестами под все 5 задач.
#Классы:
#
# Player — базовый класс (play())
#
# AudioPlayer — наследуется от Player
#
# VideoPlayer — наследуется от Player
#
# SmartPlayer — наследуется от AudioPlayer и VideoPlayer
#
# Требование:
#
# Реализовать play() во всех классах так, чтобы
#
# SmartPlayer().play()
#
#
# выводил:
#
# SmartPlayer play
# AudioPlayer play
# VideoPlayer play
# Player play
# class Player:
#     def play(self):
#         print('Player play')
# class AudioPlayer(Player):
#     def play(self):
#         print('AudioPlayer play')
#         super().play()
# class VideoPlayer(Player):
#     def play(self):
#         print('VideoPlayer play')
#         super().play()
# class SmartPlayer(AudioPlayer,VideoPlayer,Player):
#     def play(self):
#         print('SmartPlayer play')
#         super().play()
# smart_player_one =SmartPlayer()
# smart_player_one.play()
#   Задача 2. Система уведомлений
#
# Ветка: hw6_2
#
# Классы:
#
# Notifier — (send())
#
# EmailNotifier — наследуется от Notifier
#
# SMSNotifier — наследуется от Notifier
#
# MultiNotifier — наследуется от EmailNotifier и SMSNotifier
#
# Требование:
#
# Вызов:
#
# MultiNotifier().send()
#
#
# должен пройти по MRO и вывести сообщения каждого класса.
# class Notifier:
#     def send(self):
#         print(' Notifier')
#         super().send()
# class EmailNotifier(Notifier):
#     def send(self):
#         print('EmailNotifier')
#         super().send()
# class SMSNNotifier(Notifier):
#     def send(self):
#         print('SMSNNotifier')
#         super().send
# class MultiNotifier(EmailNotifier,SMSNNotifier):
#     def send(self):
#         print('MultiNotifier')
#         super().send()
#
# multiNotifier_one =MultiNotifier()
# multiNotifier_one.send()
   # Ветка: hw6_5
#
# Классы:
#
# Transport — (move())
#
# LandTransport — наследуется от Transport
#
# WaterTransport — наследуется от Transport
#
# Amphibian — наследуется от LandTransport и WaterTransport
#
# Требование:
# Amphibian().move()
#
#
# вызывает move() всех классов по MRO.
#
# 💡 Общая подсказка для всех задач:
# print(ClassName.mro())
# class Transport:
#     def move(self):
#         print('Транспорт движется куда-то')
# class LandTransport(Transport):
#     def move(self):
#         super().move()
#         print('Надземный транспорт')
# class WaterTransport(Transport):
#     def move(self):
#         super().move()
#         print('Водный транспорт')
# class Amphibian(LandTransport,WaterTransport):
#     def move(self):
#         super().move()
#         print('Плавает и едит')

# amphibian_one =Amphibian()
# print(Amphibian.mro())
# amphibian_one.move()
   # Ветка: hw6_4
#
# Классы:
#
# Logger — (log())
#
# FileLogger — наследуется от Logger
#
# ConsoleLogger — наследуется от Logger
#
# AppLogger — наследуется от FileLogger и ConsoleLogger
#
# Требование:
#
# Метод log() должен выводить информацию о порядке вызовов по MRO.
# class Logger:
#     def Log(self):
#         print('log')
# class FileLogger(Logger):
#     def Log(self):
#         print('filelog')
#         super().Log()
# class ConsoleLogger(Logger):
#     def Log(self):
#         print('consolelog')
#         super().Log()
# class AppLogger(FileLogger,Logger):
#     def Log(self):
#         print('applogger')
#         super().Log()
# appLogger_one =AppLogger()
# appLogger_one.Log()
# print(AppLogger.mro())
# from blessed import Terminal
#
# terminal = Terminal()
#
# name ={'капуста': terminal.red}
#
# for name, color in name.items():
#     print(color + name + terminal.normal)
# import sqlite3
#
#
# def create_table(connection):
#     connection.execute('DROP TABLE IF EXISTS users')
#     connection.execute("""
#     CREATE TABLE users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         surname TEXT,
#         age INTEGER,
#         floor INTEGER,
#         password INTEGER,
#         gpa REAL,
#         foto BLOB,
#         point INTEGER
#     )
#     """)
#     connection.commit()
# def marc(connection, name, surname, age, floor, password, gpa, foto, point):
#     cursor = connection.cursor()
#     cursor.execute(
#         "INSERT INTO users (name, surname, age, floor, password, gpa, foto, point) VALUES (?,?,?,?,?,?,?,?)",
#         (name, surname, age, floor, password, gpa, foto, point)
#     )
#     connection.commit()
#
# def create_mace_table(conn):
#     conn.execute("""
#     CREATE TABLE IF NOT EXISTS marks(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     users_id INTEGER,
#     subject TEXT,
#     mark INTEGER
#     )
#     """)
#     conn.commit()
#
# if __name__ == '__main__':
#     conn = sqlite3.connect('database.db')
#
#     create_table(conn)
#     marc(conn, 'Artur','Mamasakov',17,5,1234,4.4,"i'have",0)
#
#     create_mace_table(conn)
#     marc('','','','','','','','','')
#     conn.close()
import sqlite3

def create_table(conn):
    conn.execute('DROP TABLE IF EXISTS users')
    conn.execute("""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        age INTEGER,
        floor INTEGER,
        password INTEGER,
        gpa REAL,
        foto BLOB,
        point INTEGER
    )
    """)
    conn.commit()

def add_user(conn, name, surname, age, floor, password, gpa, foto, point):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, surname, age, floor, password, gpa, foto, point) VALUES (?,?,?,?,?,?,?,?)",
        (name, surname, age, floor, password, gpa, foto, point)
    )
    conn.commit()
    return cursor.lastrowid

def create_marks_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS marks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        users_id INTEGER,
        subject TEXT,
        mark INTEGER,
        FOREIGN KEY(users_id) REFERENCES users(id)
    )
    """)
    conn.commit()

def add_mark(conn, user_id, subject, mark):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO marks (users_id, subject, mark) VALUES (?,?,?)",
        (user_id, subject, mark)
    )
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_table(conn)
    create_marks_table(conn)

    user_id = add_user(conn, 'Artur', 'Mamasakov', 17, 5, 1234, 4.4, "i'have", 0)
    add_mark(conn, user_id,'Math', 4)

    conn.close()