class Animal:
    def __init__(self, age:int, gender:bool, name:str):
        self.age=age
        self.gender="Male" if gender else "Female"
        self.name=name
        
    def eat():
        pass
    def make_sound():
        pass

class Dog(Animal):
    def __init__(self, age:int, gender:bool, name:str, food:str):
        super().__init__(age, gender, name)
        self.food=food

    def make_sound(self):
        print("Dog barks!")

    def eat(self):
        print(f"Dogs eat {self.food}")

class Chicken(Animal):

    def __init__(self, age:int, gender:bool, name:str, food:str):
        super().__init__(age, gender, name)
        self.food=food

    def make_sound(self):
        print("Cluck! Cluck!")

    def eat(self):
        print(f"Chicken eats {self.food}")

class Cow(Animal):
    def __init__(self, age:int, gender:str, name:str, milk_production:int, food:str):
        super().__init__(age, gender, name)
        self.milk_production=milk_production
        self.food=food
    
    def make_sound(self):
        print("Mooooooooo")

    def eat(self):
        print(f"Cows eat {self.food}")






chicken = Chicken(1,False,"Henny", "grains")
chicken.make_sound()
chicken.eat()


dog = Dog(2,True,"Zoe","meat")
dog.make_sound()
dog.eat()


cow = Cow(4,False,"Masha",7,"grass")
cow.make_sound()
cow.eat()
