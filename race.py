import random
from elements import *
class Creature(Fire, Water):
    #Класс начальной сущности
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, 
    agility, damage):
        #нужно написать начальное значение для здоровье, и тякущие. Чтобы можно было востанавливать
        self.name = name #имя
        self.race = race #расса
        self.lvl = lvl #уровень
        self.xp = xp #опыт
        self.hp = float(hp) #жизнь
        self.mp = mp #мана
        self.sp = sp #стамина
        self.ushp = ushp #Тякущие hp
        self.usmp = usmp #Тякуще mp
        self.ussp = ussp #Тякущие sp
        self.strength = strength #сила
        self.will = will #воля
        self.intelligence = intelligence #интелект
        self.endurance = endurance #выносливость
        self.agility = agility #ловкость
        self.damage = damage #урон

        race = 'Существо'

    
    def attack(self):
        self.ussp -= 25
        if self.ussp <= 0:
            self.rest()
            print('Противник востановил силы')
        else:
            damag = (self.strength + self.agility)/2 + self.damage + random.randint(1, 20)
        return damag
    
    def power_attack(self):
        self.ussp -= 40
        if self.ussp <= 0:
            self.rest()
            print('Противник востановил силы')
        else:
            damag = (self.strength + self.agility+self.endurance)/2 + self.damage + random.randint(1, 15)
        return damag

    def rest(self):
        self.usmp = self.mp
        self.ussp = self.sp

class Human(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Человек'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)
    
    def race_ability(self):
        self.will += 2
        self.intelligence += 2
        self.hp += 30

class Elf(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Эльф'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)
    
    def race_ability(self):
        self.agility += 2
        self.intelligence += 3
        self.mp += 30

class Dwarf(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Гном'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

    def race_ability(self):
        self.will += 1
        self.endurance + 4
        self.sp += 20
        self.hp += 10

class Beastman(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Зверочеловек'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

    def race_ability(self):
        self.hp += 30
        self.damage += 10

class Goblin(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Гоблин'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

class Wolf(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Волк'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

class Ork(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Орк'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

class Bear(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Медведь'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

class Skeleton(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Скелет'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

class Spider (Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Паук'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

#Тут пошло что-то вообще не то
class Knight(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Рыцарь'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

class Peasant(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Крестьянин'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)

class Robber(Creature):
    def __init__(self, name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage):
        race = 'Разбойник'
        super().__init__(name, race, lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)
