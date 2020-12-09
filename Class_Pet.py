class Pet:
    def __init__(self, name, age, hunger, playful):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.playful = playful

    # getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful
    #setter

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setHunger(self, hunger):
        self.hunger = hunger

    def setPlayful(self, playful):
        self.playful = playful

    def __str__(self):
        return(self.name + " is " + str(self.age) + " years old ")

Pet1 = Pet("Jim", 3, False, True)
print(Pet1.getName())
print(Pet1.getPlayful())
Pet1.setName("Snowball")
print(Pet1.getName())
class Dog(Pet):
    def __init__(self, name, age, hunger, playful, breed, favoritetoy):
        Pet.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.favoritetoy = favoritetoy

    def WantsToPlay(self):
        if self.playful == True:
            return "Dog wants to play with " + self.favoritetoy
        else:
            return "Dog doesnt wants to play with his favorite toy"

huskydog = Dog("Snowball", 2, False, True, "Husky", "Stick")
print(huskydog.WantsToPlay())
huskydog.playful = False
print(huskydog.WantsToPlay())

class Cat(Pet):
    def __init__(self, name, age, hunger, playful, place):
        Pet.__init__(self, name, age, hunger, playful)
        self.FavoritePlaceToSit = place

    def WantsToSit(self):
        if self.playful == False:
            print("Cat wants to sit " + self.FavoritePlaceToSit)
        else:
            print( "Cat wants to play")

    def __str__(self):
        return self.name + " wants to sit " + self.FavoritePlaceToSit

class Human():
    def __init__(self, name, Pets):
        self.name = name
        self.pets = Pets

    def hasPets(self):
        if len(self.pets ) != 0:
            return "Yes"
        else:
            return "No"

typlicalCat = Cat("Fluffy", 2, False, False, "in the sun ray")
typlicalCat.WantsToSit()
print(typlicalCat)
print(huskydog)
averageHuman = Human("Alice", [huskydog, typlicalCat])
HasPets = averageHuman.hasPets()
print(HasPets)
print(averageHuman.pets[0])
print(averageHuman.pets[1])
print(averageHuman.pets[0].name)