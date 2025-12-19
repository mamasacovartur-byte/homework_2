### 1. Класс Contact
#
# Этот класс будет описывать один контакт. У него должны быть **атрибуты**:
#
# - `name` - имя контакта
# - `phone_number` - номер телефона
#
# Также в этом классе нужно создать **статический метод**
# `validate_phone_number(phone_number)`, который проверяет,
# что телефонный номер содержит **ровно 10 цифр**. Если номер корректный,
# метод должен возвращать `True`, иначе - `False`.
# ### 2. Класс ContactList
#
from tkinter.font import names


class Contact:
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        """проверяет телефонный номер ровно 10 цифр"""

        if len(phone_number) != 10:
            return False

        for number in phone_number:
            if number <'0' or number >'9':
                return False

        return True
class Contactlist:
    all_contacts = []

    @classmethod
    def add_contact(cls,name,phone_number):
        """новфй контакт добавлят в all_contactlisr
        перед добавлением проверяет номер телефона"""

        if not Contact.validate_phone_number(phone_number):
            print('ошибка номер телефона должен быть ровно 10 цифр')
            return 'нет такого номера'

        new_contact = Contact(name, phone_number)
        cls.all_contacts.append(new_contact)
        print(f'новый контакт {name} добавлен')
        return new_contact

Contactlist.add_contact('artur','0709632597')
print('ful contact')
for contact in Contactlist.all_contacts:
    print(contact.name, contact.phone_number)