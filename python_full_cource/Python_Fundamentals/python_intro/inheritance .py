# Define a base class Mammal
class Mammal:
    def walk(self):
        # Method to simulate walking for all mammals
        print("walk")

# Define a subclass Dog that inherits from Mammal
class Dog(Mammal):
    def bark(self):
        # Method specific to dogs
        print('bark')

# Define another subclass Cat that inherits from Mammal
class Cat(Mammal):
    def be_annoying(self):
        # Method specific to cats
        print('annoying')

# Create an instance of the Dog class
dog1 = Dog()
dog1.walk()  # Call the 'walk' method inherited from Mammal class
dog1.bark()  # Call the 'bark' method specific to Dog class

# Create an instance of the Cat class
cat = Cat()
cat.be_annoying()  # Call the 'be_annoying' method specific to Cat class
