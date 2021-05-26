from pets.pet import Pet
# from Shipwell_Training.tamagotchi_game.pets.pet import Pet

class Dog(Pet):
    sounds = ['Woof']

    def speak(self):
        print(self.sounds)

    def who_am_i(self):
        print("I am a dog!")