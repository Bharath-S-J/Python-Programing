# Define a class named Point
class Point:
    def __init__(self, x, y):
        # Constructor method (__init__) to initialize instance variables 'x' and 'y'
        self.x = x
        self.y = y
    
    def move(self):
        # Method to simulate moving the point
        print('move')
    
    def draw(self):
        # Method to simulate drawing the point
        print("draw")

# Example usage of the Point class
point = Point(10, 20)  # Create an instance of Point class with initial values for 'x' and 'y'
point.x = 11  # Modify the 'x' coordinate of the point
print(point.x)  # Print the 'x' coordinate of the point

# Define a class named Person
class Person:
    def __init__(self, name):
        # Constructor method (__init__) to initialize instance variable 'name'
        self.name = name
    
    def talk(self):
        # Method to simulate the person talking
        print(f"Hi, I am {self.name}")

# Example usage of the Person class
bharath = Person("Bharath")  # Create an instance of Person class with name "Bharath"
bharath.talk()  # Call the 'talk' method of the Person object (prints a greeting)
