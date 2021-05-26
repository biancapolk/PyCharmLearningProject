import unittest
from Shipwell_Training.tamagotchi_game.pets.pet import Pet


# from tamagotchi_main import Pet as Pet

# what to create a class for in the unit test section and what not to create a class for

# Creating a unit test to initialize the pet class and trying to reference that class in each of my other test class methods
class TestPet(unittest.TestCase):
    def setUp(self) -> None:
        self.test_pet = Pet(name='Testy', type= 'Dog', age=9)

    def tearDown(self) -> None:
        self.pet = None


class TestInit(TestPet):

    def test_initial_name(self):
        self.assertEqual('Testy', self.test_pet.name)

    def test_initial_age(self):
        self.assertEqual(8, self.test_pet.age)


class TestPets(unittest.TestCase):

    def test_clocktick(self):
        # Pet class reference from import module is needed
        alladin = Pet(name='alladin', type='Cat', age=8)
        hunger_before = alladin.hunger
        boredom_before = alladin.boredom

        alladin.clock_tick()

        # Get attributes that alladdin has post clock_tick
        self.assertEqual(alladin.age, 8.25)
        self.assertEqual(alladin.hunger, hunger_before + 1)
        self.assertEqual(alladin.boredom, boredom_before + 1)

    def test_happy(self):
        self.fail()

    def test_hungry(self):
        self.fail()

    def test_hello(self):
        self.fail()

    def test_boredom_decreases_when_speaking(self):
        self.fail()

    def test_something_else(self):
        self.fail()


class TestClock(unittest.TestCase):
    #runs twice
    def setUp(self) -> None:
        self.pet = Pet(name='Testy', type='Cat', age=8)

    #runs once
    @classmethod
    def setUpClass(cls) -> None:
        cls.pet = Pet(name='Testy', type='Cat', age=8)

    def test_mood(self):
        roxie = Pet(name='Roxie', type='Cat', age=8)
        roxie.mood()

        self.assertEqual(roxie.mood(), "happy")


class TestMood(unittest.TestCase):

    def setUp(self) -> None:
        self.pet = Pet(name='Testy', type='Cat', age=8)

    def test_mood(self):
        roxie = Pet(name='Roxie', type='Cat', age=8)
        roxie.mood()

        self.assertEqual(roxie.mood(), "happy")
