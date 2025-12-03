class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


    def introduce(self):
        introduce = ("по професия я "
            if self.higher_education
            else "нет професии")
        print(f"Меня зовут {self.name},", f"я родился {self.birth_date}", f"по профессии {self.occupation}", f"{introduce}.")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education,group_name):
        super().__init__(name,birth_date,occupation,higher_education)
        self.group_name = group_name

    def introduce(self):
        """Дополнительная информация"""
        print(f"Меня зовут {self.name}", f"я родился {self.birth_date}", f"по профессии {self.occupation} , имею {self.higher_education},мой одногрупник  {self.group_name}" )
 

classmate_one = Classmate("Artur","16.01.2008","прошраммист","среднее образование","Алмаз")
classmate_two = Classmate("Arslan","23.04.2005","врач","высшее оброзование","Алмаз")
classmate_one.introduce()
classmate_two.introduce()

class Friend(Person):
    def __init__(self,name, birth_date, occupation, higher_education,hobby,friend):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend = friend
    def introduce(self):
        """Дополнительная информация"""
        print(f"Меня зовут {self.name},", f"я родился {self.birth_date}",f',я друг {self.friend}',
                  f"по профессии {self.occupation} , имею {self.higher_education},моё хобби {self.hobby}")


friend_one = Friend("Бексултан","27.09.2000","хирург","высшее образование","бокс","Алмаза")
friend_two = Friend("Арген","15.03.2007","машинист","среднее образование","бег" , "Алмаза")
friend_one.introduce()
friend_two.introduce()