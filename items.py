class Item:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    
class Weapon(Item):
    def __init__(self, name, weight, price, damage):
        self.damage = damage
        super().__init__(name, weight, price)

    def attack(self):
        return self.damage
    
class Potion(Item):
    def __init__(self, name, weight, price, effect):
        self.effect = effect
        super().__init__(name, weight, price)

    def health_potion(self):
        helth = ['леченье', 'Зелье леченья', 'зелье леченья']
        if self.name in helth:
            effect = self.effect
        else:
            effect = 0
        return effect
    
    def stamina_potion(self):
        stamina = ['выносливость', 'Зелье выносливости', 'зелье выносливости']
        if self.name in stamina:
            effect = self.effect
        else:
            effect = 0
        return effect
        

    def mana_potion(self):
        mana = ['мана', 'Зелье маны', 'зелье маны']
        if self.name in mana:
            effect = self.effect
        else:
            effect = 0
        return effect
    
