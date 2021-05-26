from Shipwell_Training.tamagotchi_game.pets.pet import Pet


class Cat(Pet):
    sounds = ['Meow']

    def speak(self):
        print(self.sounds)

    def who_am_i(self):
        print("I am a cat!")
