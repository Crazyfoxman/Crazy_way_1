import random

class Element():
    def __init__(self, mp, usmp, intelligence, will):
        self.mp = mp
        self.usmp = usmp
        self.intelligence = intelligence
        self.will = will


    def boll(self):
        damage = (self.intelligence + self.will)/2 + random.randint(1, 20)
        self.usmp -= 25
        return damage

    def magic_wall(self):
        damage = (self.intelligence + self.will)/2 + random.randint(1, 20) + 5
        self.usmp -= 50
        return damage
    
    def magic_explosion(self):
        damage = (self.intelligence + self.will) + random.randint(1, 20)
        self.usmp -= 75
        return damage

class Fire(Element):
    def fire_boll(self):
        damage = super().boll() + random.randint(1, 10)
        self.usmp -= 33
        return damage
    
    def fire_magic_wall(self):
        damage = super().magic_wall() + random.randint(1, 10)
        self.usmp -= 63
        return damage
    
    def fire_magic_explosion(self):
        damage = super().magic_explosion() + random.randint(1, 10)
        self.usmp -= 93
        return damage
    
class Water(Element):
    def water_boll(self):
        damage = super().boll() + random.randint(1, 5)
        self.usmp -= 27
        return damage
    
    def water_magic_wall(self):
        damage = super().magic_wall() + random.randint(1, 5)
        self.usmp -= 57
        return damage
    
    def water_magic_explosion(self):
        damage = super().magic_explosion() + random.randint(1, 5)
        self.usmp -= 80
        return damage
    

