class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

Human = Person('Dilshod', 25)
# Human.change_name('Viktor')
print(Human.name)
print(Human.age)