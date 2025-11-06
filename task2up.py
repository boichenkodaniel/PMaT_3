class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
    def __str__(self):
        return f"{self.name}"

class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит Гав!"
    def fetch(self):
        return f"{self.name} приносит палку!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит Мяу!"
    def climb(self):
        return f"{self.name} лазает по деревьям!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} говорит Чик-чирик!"
    def fly(self):
        return f"{self.name} летает!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        elif animal_type == "bird":
            return Bird(name)
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")

factory = AnimalFactory()

animals = [
    factory.create_animal("dog", "Шарик"),
    factory.create_animal("cat", "Мурка"),
    factory.create_animal("bird", "Кеша")
]

for animal in animals:
    print(animal.speak())
    if isinstance(animal, Dog):
        print(animal.fetch())
    elif isinstance(animal, Cat):
        print(animal.climb())
    elif isinstance(animal, Bird):
        print(animal.fly())
    print()