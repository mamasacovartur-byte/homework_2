from HomeWork.hw_1 import Person
person_one = Person('Нурсултан','19.01.2008','Окулист','среднее образование')
person_one.introduce()
from blessed import Terminal

term = Terminal()

fruits = {"🍎 = Apple": term.red,"🍌 = Banana": term.yellow,"🍒 = Cherry": term.magenta,
          "🍇 = Grape": term.blue,"🥭 = Mango": term.green,"🍊 = Orange": term.yellow,   "🍑 = Peach": term.magenta   }

for fruit, color in fruits.items():
    print(color + fruit + term.normal)


