
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def education(self):
        return self.__higher_education

    @property
    def occupation(self):
        return self.__occupation

    def introduce(self):
        introduce ="я по образовании "
        if self.education:
            print(f'у меня есть {self.education} образование ')
        else:
            print(f' у меня нет {self.education} образования',f'{introduce}')

        if self.occupation:
            print(f'по професси я {self.occupation}')
        else:
            print(f'это не профессия {self.occupation}')

    def interesting(self):
        """Дополнительная информация"""
        print(f"Меня зовут {self.name}", f"я родился {self.birth_date}",f"по профессии {self.occupation} , имею {self.education}")


person_one = Person('Талант','23.06.1988','полицейский','среднее')
person_two = Person('Руслан','12.01.1999','сварщик','высшее')

person_one.interesting()
person_two.interesting()
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name


    def introduce(self):
        """Дополнительная информация"""
        print(f"Меня зовут {self.name}", f"я родился {self.birth_date}",
              f"по профессии {self.occupation} , имею {self.education},мой одногрупник  {self.group_name}")


classmate_one = Classmate("Artur", "16.01.2008", "прошраммист", "среднее образование", "Алмаз")
classmate_two = Classmate("Arslan", "23.04.2005", "врач", "высшее оброзование", "Алмаз")
classmate_one.introduce()
classmate_two.introduce()


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend = friend




    def introduce(self):
        """Дополнительная информация"""
        print(f"Меня зовут {self.name},", f"я родился {self.birth_date}", f',я друг {self.friend}',
              f"по профессии {self.occupation} , имею {self.education},моё хобби {self.hobby}")



friend_one = Friend("Бексултан", "27.09.2000", "хирург", "высшее образование", "бокс", "Алмаза")
friend_two = Friend("Арген", "15.03.2007", "машинист", "среднее образование", "бег", "Алмаза")
friend_one.introduce()
friend_two.introduce()