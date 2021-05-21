# create a class, use the command pass to set to undefined objects
class Pet:
    def __init__(self, name, fullness= 50, happiness = 50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self, hunger, mopiness):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness 

cujo = Pet("Cujo", 50, 0, 80, 70 )
cujo.eat_food()
print(cujo.fullness)
print(cujo.name,cujo.fullness, cujo.happiness, cujo.hunger,cujo.mopiness)
 #"Cujo"

benji = Pet("Benji", 20, 100, 5, 10)
benji.get_love()
print(cujo.fullness)
print(benji.name, benji.fullness, benji.happiness, benji.hunger, benji.mopiness)
# "benji"

lassie = Pet("Lassie", 50, 70, 15, 20)
lassie.eat_food()
print(lassie.fullness)
lassie.get_love
print(lassie.happiness)
print(lassie.name,lassie.fullness,lassie.happiness,lassie.hunger,lassie.mopiness)

