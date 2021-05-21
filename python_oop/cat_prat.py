class Cat:
    # attribute!
    species = 'mammal'

    # Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def describe(self):
        return "%s is %d years old." % (self.name, self.age)

guster = Cat("Guster", 11)
bandit = Cat("Bandit", 11)

print(guster.describe())
print(bandit.describe())