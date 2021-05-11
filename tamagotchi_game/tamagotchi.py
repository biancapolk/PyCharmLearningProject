"""A Tamagotchi Game"""
from random import randrange

class Pet:
    # Class object attribute
    # Same for any instance of a class
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10

    #Method called upon when creating an instance of a class
    def __init__(self,name = 'Dog', age = 0):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute name
        self.name = name
        self.age = age
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def clock_tick(self):
        self.age + 0.25
        self.hunger += 1
        self.borebom += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "Happy"
        else:
            return "Bored"

    # STATE
    def __str__(self):
        state = " I'm " + self.name + "."
        state = " I feel " + self.mood() + "."
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    # OPERATIONS/Actions ----> Methods

    def bark(self):
        try:
            print("WOOF! My name is {}".format(self.name))
        except:
            print("There was an error")
        else:
            pass

    def sleep(self):
        try:
            print("{} is sleeping...".format(self.name))
        except:
            print("There was an error")
        else:
            pass
    def wake(self):
        try:
            print("{} is awake now...".format(self.name))
        except:
            print("There was an error.")
        else:
            pass


if __name__ == "__main__":
    my_pet = Pet('Nea', 8)
    my_pet.bark()
    my_pet.mood()
    my_pet.wake()
    # my_pet.walk()


