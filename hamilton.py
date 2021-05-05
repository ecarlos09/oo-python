import pdb
import datetime # Module for converting to dates

# Error handling class - extend from Exception class
class LocationError(Exception):
    pass

class Character():
    _locations = [ 
        'Magic Kingdom', 
        'EPCOT', 
        'Hollywood Studios', 
        'Animal Kingdom'
    ]

    def __init__(self, name, debut):
        self._name = name
        self._debut = debut
        self._location = None

    # Prettify our constructor variables
    def __str__(self):
        return f'{self._name} the Character'

    # Instance method example
    def introduce(self, message):
        print(f'Hi my name is {self._name} and I want to say {message}')

    # Decorator example - remove need for () when invoking
    @property
    def location(self):
        return self._location

    # Example of setter for above getter
    @location.setter
    def location(self, loc):        
        if loc in type(self)._locations: # Make _locations a class property
            self._location = loc
        else:
            raise LocationError(f'{loc} is not a valid location!')

    @property
    def length_of_service(self):
        return datetime.datetime.now().year - self._debut

    # Class method example - class method receives class an argument
    @classmethod
    def list_locations(cls):
        for loc in cls._locations: # Reference the class
            print(loc)

    # Static method
    @staticmethod
    def about():
        print('Characters are everywhere!')

# Inheritance examples

class Mouse(Character):
    # def __init__(self, name, debut, fave_food):
    #     super().init(self, name, debut)
    #     self._fave_food = fave_food

    def __str__(self):
        return f'{self._name} the mouse' # in console, print(instance) to view this

class Duck(Character):
    @staticmethod
    def about():
        print('Ducks like to swim')
    
    def swim(self):
        return f'{self._name} loves to swim'

# Create instances of our classes
mickey = Character("Mickey Mouse", 1928)
minnie = Mouse("Minnie Mouse", 1928)
daisy = Duck("Daisy Duck", 1940)

pdb.set_trace()