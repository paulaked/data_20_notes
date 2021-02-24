class Animal:

    def __init__(self):
        self.alive = True
        self.breathe()

    def breathe(self):
        print("one breath in, one out")

class LandMammal(Animal):

    def __init__(self, legs):
        super().__init__()
        self.legs = legs

    def run(self):
        return "I can run!"

Horse = Animal()
Mammoth = LandMammal(4)

Horse.alive = False
print(Horse.alive)

print()