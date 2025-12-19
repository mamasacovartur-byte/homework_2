class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        introduce = ("имею высшее образование"
            if self.higher_education
            else "высшего образования нет")
        print(f"Меня зовут {self.name}", f"я родился {self.birth_date}", f"по профессии {self.occupation}", f"{introduce}.")

if __name__ == "__main__":
    person_one = Person("Артур,","16.01.2008,", "программист", True)
    person_two = Person("Акылбек,", "03.07.2000,", "медбрат", False)
    person_free = Person("Ислам,", "04.07.2001,", "архитектор", True)

    print(person_one.name, person_one.birth_date, person_one.occupation, person_one.higher_education)
    print(person_two.name, person_two.birth_date, person_two.occupation, person_two.higher_education)
    print(person_free.name, person_free.birth_date, person_free.occupation, person_free.higher_education)
    person_one.introduce()
    person_two.introduce()
    person_free.introduce()
