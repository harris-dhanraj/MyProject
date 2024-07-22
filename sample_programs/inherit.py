# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another Child class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
