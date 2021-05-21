class Cat:
    # attribute!
    species = 'mammal'

    # Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
guster = Cat("Guster", 11)
bandit = Cat("Bandit", 11)

print("%s is %d years old." % (guster.name, guster.age))
print("%s is a %s" % (guster.name, guster.species))

print("%s is %s's sister, they are both %s" % (bandit.name, guster.name, bandit.species))