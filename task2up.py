class Dog:
    def speak(self):
        return "Гав!"

class Cat:
    def speak(self):
        return "Мяу!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

factory = AnimalFactory()

dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())
print(cat.speak())