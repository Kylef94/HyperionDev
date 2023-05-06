#note, did not add many comments as code very straightforward

class Adult():

    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
            return f"{self.name} is old enough to drive!"



class Child(Adult):

    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    def can_drive(self):
        return f"{self.name} is too young to drive!"


def new_person(name, age, eye_colour, hair_colour):
    if age >= 18:
        return Adult(name, age, eye_colour, hair_colour)
    else:
        return Child(name, age, eye_colour, hair_colour)

person1 = new_person("kyle", 20, "brown", "brown")
person2 = new_person("angie", 15, "blonde", "blue")

print(person1.name)
print(person1.can_drive())
print(person2.name)
print(person2.can_drive())
