class Animal:
    def __int__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")


dog = Dog("tom")
cat = Cat("libra")
dog.speak()
cat.speak()
