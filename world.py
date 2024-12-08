import random
from race import *
from player import *
from items import *

class World(Elf, Human, Dwarf, Beastman):

    def __init__(self, location, lvl, spaun_mobs, spaun_object):
        self.location = location
        self.lvl = lvl
        self.spaun_mobs = spaun_mobs
        self.spaun_items = spaun_object

        self.nps = self.general_nps(spaun_mobs)
        
        self.items = self.general_items(spaun_object)

    def current_location(self):
        return self.location

        

    def general_nps(self, spaun_mobs):
        #список объектов сущностей
        enemy_box = []

        #имена сущностей
        enemy_box_name = []

        spaun_mobs = random.randint(1, spaun_mobs)

        #Генератор существ
        for enemy in range(0, spaun_mobs):
            modification = self.lvl * 10
            name_list = ['Аврора', 'Эльвар', 'Луиза', 'Анна', 'Нашмар', 'Кинотон', 'Холаф', 'Дагот', 'Урэль']
            name = random.choice(name_list)
            lvl = random.randint(1, 5) + modification
            xp = random.randint(1, 100) + modification
            hp = 100 + modification
            mp = 100 + modification
            sp = 100 + modification
            ushp = 100 + modification
            usmp = 100 + modification
            ussp = 100 + modification
            strength = random.randint(1, 10) + modification
            will = random.randint(1,10) + modification
            intelligence = random.randint(1,10) + modification
            endurance = random.randint(1,10) + modification
            agility = random.randint(1,10) + modification
            damage = random.randint(1,10) + modification
            enemy = random.choice([Elf(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                   Human(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                   Dwarf(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                   Beastman(name, '',  lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)])
            enemy_box.append(enemy)

        #Перекидываю имена в список
        for i in enemy_box:
            enemy_box_name.append(i.name)

        #хранилищей сущностей
        local_nps = {}
        for i in range(0, len(enemy_box)):
            local_nps[enemy_box_name[i]] = enemy_box[i]

        #Показывает каких челиков создала генерация
        #for enemy in enemy_end_box:
        #    print(f'{enemy.name}, {enemy.lvl}, {enemy.xp}, {enemy.hp}, {enemy.mp}, {enemy.sp}, {enemy.ushp}, {enemy.usmp}, {enemy.ussp}, {enemy.strength}, {enemy.will}, {enemy.intelligence}, {enemy.endurance}, {enemy.agility}, {enemy.damage}')
        self.nps = local_nps
        return self.nps
        
    

    def general_items(self, spaun_items):
        item_list = []
        name_item  = []

        spaun_items = max(1, random.randint(1, spaun_items))

        item_box = ['мусор', 'стул']
        weapon_box = ['мечь', 'копьё', 'топор', 'стальной мечь', 'двухручный мечь', 'дубинка', 'заточеная палка', 'булова', 
                'моргенштерн', 'катана', 'молоток', 'молот', 'двухручный молот', 'рапира', 'сабля', 'камень', 'палка', 'стальная сабля']
        potion_box = ['зелье леченья', 'зелье выносливости', 'зелье маны']

        for item in range(0, spaun_items):
            #генерация предметов
            for item in item_box:
                item = random.choice(item_box)

                if item in ['мусор', 'стул']:
                    nameItem = item
                    weightItem = 5
                    priceItem = 0


            #генерация оружия
            for item in weapon_box:
                item = random.choice(weapon_box)

                #базовые оружия
                if item in ['мечь', 'топор', 'копьё', 'сабля']:
                    nameWeapon = item
                    weightWeapon = 2.5
                    priceWeapon = 100
                    damage = 10

                #стальноое оружие
                if item in ['стальной мечь', 'стальное копьё', 'стальной топор', 'стальная сабля']:
                    nameWeapon = item
                    weightWeapon = 3
                    priceWeapon = 150
                    damage = 15
                
                #всякая бесполезная фигня
                if item in ['палка', 'дубинка', 'камень', 'заточеная палка']:
                    nameWeapon = item
                    weightWeapon = 1
                    priceWeapon = 10
                    damage = 3

                #нормас оружие
                if item in ['катана', 'рапира']:
                    nameWeapon = item
                    weightWeapon = 2.5
                    priceWeapon = 200
                    damage = 20

                #Тяжёлое оружие
                if item in ['моргенштерн', 'двухручный молот', 'булова']:
                    nameWeapon = item
                    weightWeapon = 4
                    priceWeapon = 250
                    damage = 200


            #генерация зелий
            for item in potion_box:
                item = random.choice(potion_box)

                if item in ['зелье леченья', 'зелье выносливости', 'зелье маны']:
                    namePotion = item
                    weightPotion = 2.5
                    pricePotion = 100
                    effect = 10
               
               
            item = random.choice([Item(nameItem, int(weightItem), priceItem),
                                Weapon(nameWeapon, int(weightWeapon), priceWeapon, damage),
                                Potion(namePotion, int(weightPotion), pricePotion, effect)])
            item_list.append(item)

            for i in item_list:
                name_item.append(i.name)

            
            local_items = {}
            for i in item_list:
                local_items[i] = i.name

        self.items = local_items
        return self.items

            

    def fait(self):
        #хранит NPS
        enemy_values = []
        for i in self.nps:
            a = self.nps[i]
            enemy_values.append(a)

        #Ключи к словарю с NPS    
        enemy_key = [i for i in self.nps]

        #Показ того, кто на тебя напал
        print('******************************')
        for enemy in enemy_key:
            print(f'На тебя напал {self.nps[enemy].race}\n')


        for enemy in enemy_values:
            enemy_attack_list = [enemy.attack(), enemy.power_attack(), enemy.fire_boll(), enemy.water_boll(), enemy.fire_magic_wall(), enemy.water_magic_wall()]
            while True:
            #Цикл сражения с толпой врагов

                #проверка на то умер ли враг
                if enemy.hp <= 0:
                    print(f'{enemy.race} Проиграл')
                    del self.nps[enemy.name]

                    #проверка на то умерли ли все враги
                    if len(self.nps) == 0:
                        print('Все были убиты')
                        break
                    break

                #Смерть игрока
                if player.ushp <= 0:
                    print(f'{player.name} Проиграл')
                    break

                print('******************************') 
                print(f'Перед тобой стоит {enemy.race}')
                print(f'Действия:\n*атаковать\n*силовая атака\n*огненый шар\n*водяной шар\n*огненная стена\n*водяная стена\n*водяной взрыв\n*огнеенный взрыв')

                do = input('Что ты будешь делать? ')
                enemy_attack = random.choice(enemy_attack_list)


                if do == 'атаковать':
                    enemy.hp -= player.attack()
                if do == 'силовая атака':
                    enemy.hp -= player.power_attack()
                if do == 'огненый шар':
                    enemy.hp -= player.fire_boll()
                if do == 'водяной шар':
                    enemy.hp -= player.water_boll()
                if do == 'огненная стена':
                    enemy.hp -= player.fire_magic_wall()
                if do == 'водяная стена':
                    enemy.hp -= player.water_magic_wall()
                if do == 'огненный взрыв':
                    enemy.hp -= player.fire_magic_explosion()
                if do == 'водяной взрыв':
                    enemy.hp -= player.water_magic_explosion()
                if do == 'отдых':
                    player.rest()

                print(f'Хп {enemy.race}, равно {enemy.hp}')

                player.ushp -= enemy_attack
                print(f'Твоё хп {player.ushp}')


class Forest(World):
    def __init__(self, location, lvl, spaun_mobs, spaun_items):
        super().__init__(location, lvl, spaun_mobs, spaun_items)

    def general_nps(self, spaun_mobs):
        #список объектов сущностей
        enemy_box = []

        #имена сущностей
        enemy_box_name = []

        spaun_mobs = random.randint(1, spaun_mobs)

        #Генератор существ
        for enemy in range(0, spaun_mobs):
            modification = self.lvl * 10
            name_list = ['Аврора', 'Эльвар', 'Луиза', 'Анна', 'Нашмар', 'Кинотон', 'Холаф', 'Дагот', 'Урэль']
            name = random.choice(name_list)
            lvl = random.randint(1, 5) + modification
            xp = random.randint(1, 100) + modification
            hp = 100 + modification
            mp = 100 + modification
            sp = 100 + modification
            ushp = 100 + modification
            usmp = 100 + modification
            ussp = 100 + modification
            strength = random.randint(1, 10) + modification
            will = random.randint(1,10) + modification
            intelligence = random.randint(1,10) + modification
            endurance = random.randint(1,10) + modification
            agility = random.randint(1,10) + modification
            damage = random.randint(1,10) + modification
            enemy = random.choice([Elf(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Wolf(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Ork(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Goblin(name, '',  lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Bear(name, '',  lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)])
            enemy_box.append(enemy)

        #Перекидываю имена в список
        for i in enemy_box:
            enemy_box_name.append(i.name)

        #хранилищей сущностей
        nps = {}
        for i in range(0, len(enemy_box)):
            nps[enemy_box_name[i]] = enemy_box[i]

        #Показывает каких челиков создала генерация
        #for enemy in enemy_end_box:
        #    print(f'{enemy.name}, {enemy.lvl}, {enemy.xp}, {enemy.hp}, {enemy.mp}, {enemy.sp}, {enemy.ushp}, {enemy.usmp}, {enemy.ussp}, {enemy.strength}, {enemy.will}, {enemy.intelligence}, {enemy.endurance}, {enemy.agility}, {enemy.damage}')
        return nps
    
    def general_items(self, spaun_items):
        return super().general_items(spaun_items)

class Dungeon(World):
    def __init__(self, location, lvl, spaun_mobs, spaun_items):
        super().__init__(location, lvl, spaun_mobs, spaun_items)

    def general_nps(self, spaun_mobs):
        #список объектов сущностей
        enemy_box = []

        #имена сущностей
        enemy_box_name = []

        spaun_mobs = random.randint(1, spaun_mobs)

        #Генератор существ
        for enemy in range(0, spaun_mobs):
            modification = self.lvl * 10
            name_list = ['Аврора', 'Эльвар', 'Луиза', 'Анна', 'Нашмар', 'Кинотон', 'Холаф', 'Дагот', 'Урэль']
            name = random.choice(name_list)
            lvl = random.randint(1, 5) + modification
            xp = random.randint(1, 100) + modification
            hp = 100 + modification
            mp = 100 + modification
            sp = 100 + modification
            ushp = 100 + modification
            usmp = 100 + modification
            ussp = 100 + modification
            strength = random.randint(1, 10) + modification
            will = random.randint(1,10) + modification
            intelligence = random.randint(1,10) + modification
            endurance = random.randint(1,10) + modification
            agility = random.randint(1,10) + modification
            damage = random.randint(1,10) + modification
            enemy = random.choice([Dwarf(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Skeleton(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Ork(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Goblin(name, '',  lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Spider(name, '',  lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)])
            enemy_box.append(enemy)

             #Перекидываю имена в список
        for i in enemy_box:
            enemy_box_name.append(i.name)

        #хранилищей сущностей
        nps = {}
        for i in range(0, len(enemy_box)):
            nps[enemy_box_name[i]] = enemy_box[i]

        #Показывает каких челиков создала генерация
        #for enemy in enemy_end_box:
        #    print(f'{enemy.name}, {enemy.lvl}, {enemy.xp}, {enemy.hp}, {enemy.mp}, {enemy.sp}, {enemy.ushp}, {enemy.usmp}, {enemy.ussp}, {enemy.strength}, {enemy.will}, {enemy.intelligence}, {enemy.endurance}, {enemy.agility}, {enemy.damage}')
        return nps

    def general_items(self, spaun_items):
        return super().general_items(spaun_items)
    

class City(World):
    def __init__(self, location, lvl, spaun_mobs, spaun_items):
        super().__init__(location, lvl, spaun_mobs, spaun_items)

    def general_nps(self, spaun_mobs):
        #список объектов сущностей
        enemy_box = []

        #имена сущностей
        enemy_box_name = []

        spaun_mobs = random.randint(1, spaun_mobs)

        #Генератор существ
        for enemy in range(0, spaun_mobs):
            modification = self.lvl * 10
            name_list = ['Аврора', 'Эльвар', 'Луиза', 'Анна', 'Нашмар', 'Кинотон', 'Холаф', 'Дагот', 'Урэль']
            name = random.choice(name_list)
            lvl = random.randint(1, 5) + modification
            xp = random.randint(1, 100) + modification
            hp = 100 + modification
            mp = 100 + modification
            sp = 100 + modification
            ushp = 100 + modification
            usmp = 100 + modification
            ussp = 100 + modification
            strength = random.randint(1, 10) + modification
            will = random.randint(1,10) + modification
            intelligence = random.randint(1,10) + modification
            endurance = random.randint(1,10) + modification
            agility = random.randint(1,10) + modification
            damage = random.randint(1,10) + modification
            enemy = random.choice([Human(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Peasant(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Robber(name, '', lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Knight(name, '',  lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage),
                                    Beastman(name, '',  lvl, xp, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, agility, damage)])
            enemy_box.append(enemy)

             #Перекидываю имена в список
        for i in enemy_box:
            enemy_box_name.append(i.name)

        #хранилищей сущностей
        nps = {}
        for i in range(0, len(enemy_box)):
            nps[enemy_box_name[i]] = enemy_box[i]

        #Показывает каких челиков создала генерация
        #for enemy in enemy_end_box:
        #    print(f'{enemy.name}, {enemy.lvl}, {enemy.xp}, {enemy.hp}, {enemy.mp}, {enemy.sp}, {enemy.ushp}, {enemy.usmp}, {enemy.ussp}, {enemy.strength}, {enemy.will}, {enemy.intelligence}, {enemy.endurance}, {enemy.agility}, {enemy.damage}')
        return nps

    def general_items(self, spaun_items):
        return super().general_items(spaun_items)



