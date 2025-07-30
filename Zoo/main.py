class Animal:
    def __init__(self,name,age,health=100,happines=100):
        self.name=name
        self.age=age
        self.health=health
        self.happines=happines

    def display_info(self):
        print(f"name:{self.name} age:{self.age} Health:{self.health} Happiness:{self.happines}")
        return self
    
    def feed(self):
        self.health+=10
        self.happines+=10
        return self

class Lion(Animal):
    def __init__(self, name, age=3, mane_size="Large"):
        super().__init__(name, age, health=80, happines=90)
        self.mane_size=mane_size
    
    def feed(self):
        self.health+=15
        self.happines+=5
        print(f"{self.name} the lion roars happily!")
        return self
    
class Tiger(Animal):
    def __init__(self, name, age=2, favorite_fruit="Banana"):
        super().__init__(name, age, health=70, happines=110)
        self.favorite_frute=favorite_fruit
    
    def feed(self):
        self.health+=5
        self.happines+=20
        print(f"{self.name} the Tiger jumps with joy!")
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append(Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()