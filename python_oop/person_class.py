class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person, self.name))

    def print_contact_info(self):
        print(self.email)
        print(self.phone)

sonny = Person("Sonny","sonny@hotmail.com","(483) 485-4948")
print(sonny.name,sonny.email,sonny.phone)
#sonny

#sonny.greet("jordan")
sonny.print_contact_info()

jordan = Person("Jordan","jordan@aol.com","(495) 586-3456")
print(jordan.name, jordan.email, jordan.phone)
#jordan
jordan.print_contact_info
