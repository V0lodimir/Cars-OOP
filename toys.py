class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def purchase_material(self):
        print("Buying materials...")
    
    def tailoring(self):
        print("Tailoring...")

    def dyeing(self):
        print("Dyeing...")

class Bear(Toy):
    def creating_toy(self):
        print("Toy {} with color {} and type {} was created!".format(self.name, self.color, self.toy_type))

class Dog(Toy):
    def creating_toy(self):
        print("Toy {} with color {} and type {} was created!".format(self.name, self.color, self.toy_type))

class Cat(Toy):
    def creating_toy(self):
        print("Toy {} with color {} and type {} was created!".format(self.name, self.color, self.toy_type))

toys = [
    Bear("Teddy", "Brown", "Bear"),
    Bear("Meddy", "White", "Bear"),
    Dog("Sharik", "Brown", "Dog"),
    Cat("Berserk", "Black", "Cat")
]

for toy in toys:
    toy.purchase_material()
    toy.tailoring()
    toy.dyeing()
    toy.creating_toy()