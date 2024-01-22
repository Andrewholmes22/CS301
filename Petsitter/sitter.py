import datetime

class Pet():
#we expect the birthday to be formatted
    def __init__(self, name, birthday, owner ,color):
        self.name=name
        self._birthdate=datetime.datetime.strptime(birthday,'%m/%d/%Y')
        self._owner=owner
        self.color=color
    def printInfo(self):
        print("my name is "+self.name)
        print("my birthday is:"+self._birthdate.strftime('%m/%d/%Y'))
        print("my owners name is "+self._owner)
        print("i am "+self.color+ " in color")
    def getOwner(self):
        print("Owner: "+ self.owner)
        return self.owner
    def getAge(self):
        current_time = datetime.datetime.now()
        age = current_time - self.__birthday
        print("Age: "+ str(age.days//365)+"years")
        return age
class Dog(Pet):
    def init(self, name, birthday, owner, color, species, food):
        Pet.init(self, name, birthday, owner, color)
        self.species = species
        self.food = food
    def printInfo(self):
        Pet.printInfo(self)
        print("Species: "+self.species)
        print("Food preference: "+self.food)
    def getAge(self):
        age = Pet.getAge(self)
        dog_age = 7*age
        print("Age: "+str(dog_age//365)+" dog years")
        return age
class Cat(Pet):
    def init(self, name, birthday, owner, color, species, food):
        super.init(self, name, birthday, owner, color)
        self.species = species
        self.food = food
    def printInfo(self):
        super.printInfo(self)
        print("Species: "+self.species)
        print("Food preference: "+self.food)
    def getAge(self):
        age = Pet.getAge(self)
        Cat_age = 6*age
        print("Age: "+str(Cat_age//365)+" cat years")
        return age

new_dog = Pet("loki", "12/12/2022", "Alex", "Brown","aussie","carrot")
new_dog.printInfo()
new_dog.getOwner()
new_dog.getAge()
