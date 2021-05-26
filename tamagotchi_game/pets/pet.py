from random import randrange

class Pet:
    # Class object attribute
    # Same for any instance of a class
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    state = ""

    # Method called upon when creating an instance of a class
    def __init__(self, name, type, age):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute name
        self.name = name
        self.type = type
        self.age = age
        # Assign it using self.attribute name
        print("PET CREATED")
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    # STATE
    def clock_tick(self):
        self.age += 0.25
        self.hunger += 1
        self.boredom += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = " I'm " + self.name + "."
        state = " I feel " + self.mood() + "."
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    # OPERATIONS/Actions ----> Methods

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        print("My name is {} ".format(self.name) + " and right now I am " + self.mood() + ".")
        self.reduce_boredom()

    def sleep(self):
        pass

    def wake(self):
        pass

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
