import random

from attributes import Agile, Sneaky
from characters import Character


#Order matters in inheritance, method resolution order ('MRO')
# Move Character to the end to be the "final class"
#class Thief(Character, Agile, Sneaky):
class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))