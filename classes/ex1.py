class Cat:
    # attributes, fields, class members, properties
    color = 'black'
    breed = 'persian'
    age = 2

    # methods/functions
    def eat(self):
        print('cat is eating')

    def play(self):
        print('cat is playing')

    def description(self):
        print(f'cat is {self.age} years old')
        print(f'cat is {self.color} in color')
        print(f'cat is {self.breed} breed')

# object 
tom = Cat() # to call the constructor the class

tom.eat()
tom.play()
tom.description()

tom.age = 3
tom.breed = 'street cat'
tom.color = 'grey'

print("color", tom.color)
print('age', tom.age)

tom.description()