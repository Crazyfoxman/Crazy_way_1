import random
from elements import *
from race import *
from items import *

class Player(Human, Elf, Dwarf, Beastman):

    inventory_check_info = {}
    inventory = {}

    #Класс начальной сущности
    def __init__(self, name, race, lvl, xp, point, hp, mp, sp, ushp, usmp, ussp, strength, will, intelligence, endurance, 
    agility, damage, carry_weight, us_item):
    #нужно написать начальное значение для здоровье, и тякущие. Чтобы можно было востанавливать
        self.name = name #имя
        self.race = race #Расса
        self.lvl = lvl #уровень
        self.xp = xp #опыт
        self.point = point #Свободные очки
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
        self.carry_weight = carry_weight #переносимый вес
        self.carry_weight = self.sp
        self.us_item = us_item #используеющийся предмет

        self.lvl_up()
        
    
    def lvl_up(self):
        if self.xp == 100:
            self.lvl = 1
            self.xp -= 100
            self.point += 5

        if self.xp == 200:
            self.lvl = 2
            self.xp -= 200
            self.point += 5

        if self.xp == 300:
            self.lvl = 3
            self.xp -= 300
            self.point += 5

        if self.xp == 400:
            self.lvl = 4
            self.xp -= 400
            self.point += 5

        if self.xp == 500:
            self.lvl = 5
            self.xp -= 500
            self.point += 5

        if self.xp == 600:
            self.lvl = 6
            self.xp -= 600
            self.point += 5

        if self.xp == 700:
            self.lvl = 7
            self.xp -= 700
            self.point += 5

        if self.xp == 800:
            self.lvl = 8
            self.xp -= 800
            self.point += 5

        if self.xp == 900:
            self.lvl = 9
            self.xp -= 900
            self.point += 5

        if self.xp == 1000:
            self.lvl = 10
            self.xp -= 1000
            self.point += 5

    #Создание персонажа
    def character_creation(self):
        print('******************************')
        print('Для начала игры тебе необходимо создать персонажа. \n')
        self.name = input('Как тебя зовут? ')
        print('******************************')
        print('Существующие рассы: человек, эльф, гном, зверочеловек')
        human = ['Человек', 'человек']
        dwarf = ['Гном', 'гном']
        elf = ['Эльф', 'эльф']
        beastman = ['Зверочеловек', 'зверочеловек']
        all_race = human + dwarf + elf + beastman
        
        while True:
            race = input('Какая расса? ')
            if race in all_race:
                self.race = race
                if race in human:
                    Human.race_ability(self)
                    break

                elif race in elf:
                    Elf.race_ability(self)
                    break

                elif race in dwarf:
                    Dwarf.race_ability(self)
                    break

                elif race in beastman:
                    Beastman.race_ability(self)
                    break

                else:
                    print('Расса выбрана, накинуты дополнительные баффы')
                    print('******************************')
                    break
            else:
                print('Такой рассы нет')
                continue
        
        print('******************************')
        print('Тебе нужно раскидать очки характеристик для персанажа их 32.')
        print('Характеристики: сила, ловкость, выносливость, воля, интелект')


        strength = ['Сила', 'сила']
        will = ['Воля', 'воля']
        intelligence = ['Интелект', 'интелект']
        endurance = ['Выносливость', 'выносливость']
        agility = ['Ловкость', 'ловкость']
        all_character = strength + will + intelligence + endurance + agility

        #переменная для проверки
        all_point = 0
        #Цикл для раскидывания характеристик
        while True:
            if all_point == 32:
                    print('Отлично, очки распределены правельно')
                    print('******************************')
                    break
            
            do = input('Выбери характеристику: ')

            if do in all_character:
                point = int(input('Сколько очков назначить? '))
                print('******************************')

                if do in strength:
                    self.strength += point
                    all_point += point


                elif do in will:
                    self.will += point
                    all_point += point

                elif do in intelligence:
                    self.intelligence += point
                    all_point += point

                elif do in endurance:
                    self.endurance += point
                    all_point += point

                elif do in agility:
                    self.agility += point
                    all_point += point

            else:
                print('Нет такой характеристики')
                continue

            print(f'Сила {self.strength}\nВоля {self.will}\nЛовкость {self.agility}\nИнтелект {self.intelligence}\nВыносливость {self.endurance}\nВсего ты распределил {all_point}, нужно 32')
            print('******************************')

            if do in all_character:

                if all_point > 32:
                    do = input('Выбери характеристику у которой отнять очки: ')
                    point = int(input('Сколько очков отнять? '))
                    if do in strength:
                        self.strength -= point
                        all_point -= point

                    elif do in will:
                        self.will -= point
                        all_point -= point

                    elif do in intelligence:
                        self.intelligence -= point
                        all_point -= point

                    elif do in endurance:
                        self.endurance -= point
                        all_point -= point

                    elif do in agility:
                        self.agility -= point
                        all_point -= point

                        print(f'Сила {self.strength}\nВоля {self.will}\nЛовкость {self.agility}\nИнтелект {self.intelligence}\nВыносливость {self.endurance}\nВсего ты распределил {all_point}, нужно 32')
                        print('******************************')

            else:
                print('Нет такой характеристики')
                continue
                


        return print(f'Персонаж по имени {self.name} был создан')    

    #Распределение имеющихся очков
    def characteristics_point(self, point):
        print('Существующие характеристики(сила, воля, ловкость, интелект, выносливость)')
        do = input('Какую характеристику повысить? ')
        strength = ['Cила', 'сила']
        will = ['Воля', 'воля']
        intelligence = ['Интелект', 'интелект']
        endurance = ['Выносливость', 'Выносливость']
        agility = ['Ловкость', 'ловкость']

        while True:
            #Проверка на наличие очков
            if self.point <= 0:
                break

            if do in strength:
                self.strength += point
                self.point -= point
                break

            elif do in will:
                self.will += point
                self.point -= point
                break

            elif do in intelligence:
                self.intelligence += point
                self.point -= point
                break

            elif do in endurance:
                self.endurance += point
                self.point -= point
                break

            elif do in agility:
                self.agility += point
                self.point -= point
                break

            else:
                print('Нет такой характеристики')
                continue
    #Для проверки текущих характеристик
    def check_characteristics(self):
        return print(f'Сила {self.strength}\nВоля {self.will}\nЛовкость {self.agility}\nИнтелект {self.intelligence}\nВыносливость {self.endurance}\nСвободные очки {self.point}')

    #Окно персонажа, отображается в меню
    def check_character_window(self):
        print('******************************')
        return print(f'ОКНО ПЕРСАНАЖА {self.name}\nЗдоровье {self.ushp}\nМана {self.usmp}\nЗапас сил {self.ussp}\n\nХАРАКТЕРИСТИКИ\nСила {self.strength}\nВоля {self.will}\nЛовкость {self.agility}\nИнтелект {self.intelligence}\nВыносливость {self.endurance}\n\nСвободные очки {self.point}\n\nИспользуемое оружие {self.us_item.name}\nТякущий урон {self.current_damage}+ 1-20\n******************************')

    #Для показа текущего состояния
    def check_status(self):
        return print(f'Здоровье {self.ushp}\nМана {self.usmp}\nЗапас сил {self.ussp}')
    
    #текущий урон
    def current_damage(self):
        damag = (self.strength + self.agility+self.endurance)/2 + self.damage + self.us_item.damage
        return damag

    #обычная атака
    def attack(self):
        self.ussp -= 25
        if self.ussp <= 0:
            print('Не достаточно запаса сил, нужно отдохнуть')
            damag = 0
        else:
            damag = (self.strength + self.agility)/2 + self.damage + random.randint(1, 20) + self.us_item.damage
        return damag
    
    def power_attack(self):
        self.ussp -= 40
        if self.ussp <= 0:
            damag = 'Не достаточно запаса сил, нужно отдохнуть'
        else:
            damag = (self.strength + self.agility+self.endurance)/2 + self.damage + random.randint(1, 20) + self.us_item.damage
            print(f'Использовано оружие {self.us_item.name}')
        return damag


    #отдых(полное востановление)
    def rest(self):
        self.ushp = self.hp
        self.usmp = self.mp
        self.ussp = self.sp

    #Взять предмет
    def give_item(self, items):
        weight = self.max_carry_weight()

        #хранятся именна предметов
        value_item = [i for i in items.values()] #использую 1 раз для drop

        #хранятся сами объекты
        key_item = []
        for i in items:
            key_item.append(i)
        
        #хранит имена предметов, и склоько их
        drop = {}
        for i in value_item:
            drop[i] = value_item.count(i)

        non_save_drop = {}
        for i in value_item:
            non_save_drop[i] = value_item.count(i)
        
        #выводит выпавшие предметы
        print('************************')
        print('Найдены вещи:')
        for i in non_save_drop:
            print(f'{i}:{non_save_drop[i]}')

        flag = True

        while flag:
            if len(non_save_drop) == 0:
                print('Сбор предметов закончен')
                break

            do = input('Какой предмет будешь брать?: ')

            if weight > self.carry_weight:
                print('У тебя перегрус, избався от лишнего веса')
                break

            
            for item in drop:
                if do == item:
                    count = input('Сколько возмёшь?: ')


                    if count.isdigit() == True:
                        if int(count) > non_save_drop[item]:
                            print('Ты не можешь взять больше чем есть')
                            break
                        if int(count) < 0:
                            print('Ты не можешь брать отрицательными значеньями!')
                            break

                        if item in self.inventory_check_info:
                            self.inventory_check_info[item] += int(count)

                            for j in range(0, int(count)):
                                for i in items:
                                    if i.name == item:
                                        self.inventory[i] = item

                        if item not in self.inventory_check_info:
                            self.inventory_check_info[item] = int(count)
                            for j in range(0, int(count)):
                                for i in items:
                                    if i.name == item:
                                        self.inventory[i] = item

                        non_save_drop[item] -= int(count)

                        print(player.inventory)
                        if non_save_drop[item] <= 0:
                            del non_save_drop[item]

                        print('**************************')
                        print('Оставшиеся предметы')
                        for i in non_save_drop:
                            print(f'{i}:{non_save_drop[i]}')
                    else:
                        print('Должны быть цыфры')

                if do == 'выход':
                    flag = False

    #функция, чтобы взять 1 предмет, а не последовательность предметов
    def give_one_item(self, item):
        if item.name in self.inventory_check_info:
            self.inventory_check_info[item.name] += 1
            self.inventory[item] = item.name

        if item.name not in self.inventory_check_info:
            self.inventory_check_info[item.name] = 1
            self.inventory[item] = item.name

    #функция показывает инвентарь
    def check_inventory(self):
        if len(self.inventory_check_info) == 0:
            print('Инвентарь пустой')
        for i in self.inventory_check_info:
            print(f'{i}:{self.inventory_check_info[i]}')
        print('******************************')

    #функция выводит вес вещей в инвенторе
    def max_carry_weight(self):
        weight = 0
        for item in self.inventory:
            weight += item.weight
        return weight
    
    #функция для исплоьзования оружия
    def us_item_weapon(self):
         flag = True
         while flag:
            do = input('Какое оружие ты будешь исплоьзовать?: ')
            for item in self.inventory:

                if do == item.name:
                    if hasattr(item, 'damage'):
                        self.us_item = item
                        print(f'Было экипировано оружие {item.name}')
                        flag = False
                        break

                    if hasattr(item, 'damage') == False:
                        print(f'Ты не можешь использовать {item.name} в качестве оружия')


 
 
us_item = Weapon('мечь',2.5, 100, 10)

player = Player('Игрок', 'существо', 0, 0, 0, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 10, 100, us_item)


"""
while True:
    do = input('Твои действия?: ')

    if do == 'выход':
        break

    if do == 'повысить уровень':
        xp = int(input('Сколько накинуть очков? '))
        player.xp += xp
        player.lvl_up()
        print(player.xp, player.lvl, player.point)
    
    if do == 'повысить хары':
        print(f'у тебя {player.point} свободных очков')
        point = int(input('На сколько повысить? '))
        player.characteristics_point(point)


"""