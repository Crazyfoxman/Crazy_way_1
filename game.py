#Начал создавать игру на 50 часу обучения python. Это моя не первая попытка учить python. Но теперь я этим занялся серьёзно
from elements import *
from klass import *
from player import *
from world import *

#Создание персонажа
player.character_creation()


def menu():
    global flag
    flag = True
    while flag:
        print('******************************')
        print('Вот тебе меню игры:\n\nпродолжить игру\nокно персонажа\nинвентарь\nвыйти из игры')
        print('******************************')
        do = input('Выбери пункт меню: ')
        print('******************************')

        if do =='продолжить игру':
            return print('Игра продолжается')
        
        elif do == 'окно персонажа':
            player.check_character_window()

        elif do == 'инвентарь':
            player.check_inventory()
        

        #не доступно игроку, показывает объекты в инвентаре
        elif do == 'Инв':
            print(player.inventory)
        
        elif do == 'выйти из игры':
            print('Ты завершил игру, сохранений нет. Бывай')
            flag = False

        else:
            print('Нет такого пункта в меню')


def player_do():
    print('******************************')
    print('ДЕЙСТВИЯ С ПЕРСОНАЖЕМ:\n*сменить оружие\n*показать стутус\n*повысить уровень\n*повысить хары')
    do = input('Выбери: ')
    if do == 'сменить оружие':
        player.us_item_weapon()

    if do == 'показать статус':
        player.check_status()

    if do == 'повысить уровень':
        xp = int(input('Сколько накинуть очков? '))
        player.xp += xp
        player.lvl_up()
        print(player.xp, player.lvl, player.point)
    
    if do == 'повысить хары':
        print(f'у тебя {player.point} свободных очков')
        point = int(input('На сколько повысить? '))
        player.characteristics_point(point)

    

def travel(location):
    print('******************************')
    print(f'Тякущее местоположение {location.location}')
    print('КУДА ПОЙДЁМ?:\n*столица Империи\n*лес Эленофей\n*скалистая область\n*город Безил\n')
    do = input('Выбери: ')

    if do == 'столица Империи':
        capital_of_the_empire = City('Столица Империи', 50, 20, 25)
        location = capital_of_the_empire

    elif do == 'лес Эленофей':
        elenofey_forest = Forest('Лес Эленофей', 1, 2, 3)
        location = elenofey_forest

    elif do == 'скалистая область':
        rocky_area = Dungeon('Скалистая область', 1, 2, 3)
        location = rocky_area

    elif do == 'город Безил':
        city_of_Basil = City('Город Безил', 25, 10, 25)
        location = city_of_Basil

    else:
        print('Такой локации не существует')

    return location

def training():
    print('******************************')
    print('ПРОКАЧКА:')

def peaceful_actions():
    print('******************************')
    print('МИРНЫЕ ДЕЙСТВИЯ:\n*вздремнуть')
    do = input('Выбери: ')
    if do == 'вздремнуть':
        player.rest()
        print(f'{player.name} отдохнул, статы востановлены')





#цикл миню
print('******************************')
print('Вот тебе меню игры:\n\nпродолжить игру\nокно персонажа\nинвентарь\nвыйти из игры')
print('******************************')
flag = True
while flag:
    do = input('Выбери пункт меню: ')
    print('******************************')

    if do =='продолжить игру':

        print('Тут идёт игровой процесс')

        #Цикл игры(Главный цикл)
        while flag:
            print('******************************')
            print('Ты очнулся около потухшего костра, вокруг не души...')
            print('По лучам солнца можно понять, что сейчасс ранее утро, твоя голова раскалывается и ты мало что помнишь, о том, кто ты и что тут забыл')
            print('Осмотревшись ты нашёл мечь, ну и всё, больше ничего нет. Что же ты будешь делать?')

            forest = World('лес',1, 1, 5)
            location = forest

            print('Вот тебе список действий, которые ты можешь совершать во время игры:\n*начать путешествие\n*меню')
            print('******************************')
            do_player = input('Что ты будешь делать?: ')

            if do_player == 'начать путешествие':
                print('Ты идёшь совершенно не зная дороги, и спустя время ты выходишь на дорогу.\nНа дороге не души, но ты продолжаешь идти по ней в перёд\nКак вдруг слышен какой-то шелест в кустах')
                forest.fait()
                print('******************************')
                print('Выпали предметы')
                player.give_item(forest.items)

                print('Враг был повержен')
                print('Ты осматриваешь труп и находишь записку')
                print('******************************')
                print('От Альфреда')
                print('Так, жди меня окло дороги, у старой Ивы. Я буду ближу к обеду.\nСмотри мне, хоть кого-либо грабанёшь без меня\nбудешь потом без еды сидеть\n\nИ да, карту взять не забудь, есть одно дело')

                karta = Item('Карта Империи', 0.1, 100)
                player.give_one_item(karta)
                print('Поздравляю, теперь ты можешь перемещаться по Империи')





                while flag:
                    print('******************************')
                    print(f'Текущая локация {location.location}')
                    if location.location == 'Столица Империи':
                        print('Ты находишься в Центральном городе Империи, тут слоняются разного рода люди, эльфы, гномы и зверолюди')
                        capital_of_the_empire = City('Столица Империи', 50, 20, 25)
                        location = capital_of_the_empire
                        print('******************************')

                    if location.location == 'Лес Эленофей':
                        print('Ты находишься в лесу Эленофей, эта територия кешит различного рода существами, кто знает, что может случится, если потерять бдительность')
                        elenofey_forest = Forest('Лес Эленофей', 1, 2, 3)
                        location = elenofey_forest
                        print('******************************')

                    if location.location == 'Скалистая область':
                        print('Ты находишься в скалистой области, место довольно удручающие.\nТут живут гномы, но в основном встречаются разные твари')
                        rocky_area = Dungeon('Скалистая область', 1, 2, 3)
                        location = rocky_area
                        print('******************************')

                    if location.location == 'Город Безил':
                        print('Ты находишься в городе Безил. Довольно тихое местечко')
                        city_of_Basil = City('Город Безил', 25, 10, 25)
                        location = city_of_Basil
                        print('******************************')

                    print('Вот тебе список действий, которые ты можешь совершать во время игры:\n*действия с персонажем\n*мирные действия\n*начать сражаться\n*путешествовать\n*меню')
                    print('******************************')
                    do = input('Что выберешь?: ')

                    if do == 'действия с персонажем':
                        player_do()

                    if do == 'мирные действия':
                        peaceful_actions()

                    if do == 'начать сражаться':
                        print('Ты решил напасть на кого попало')
                        location.fait()
                        player.give_item(location.items)


                    if do == 'путешествовать':
                        location = travel(location)
                        
                    if do == 'меню':
                        menu()







            if do_player == 'меню':
                break


    elif do == 'окно персонажа':
        player.check_character_window()

    elif do == 'инвентарь':
        player.check_inventory()
    

    #не доступно игроку, показывает объекты в инвентаре
    elif do == 'Инв':
        print(player.inventory)
    
    elif do == 'выйти из игры':
        print('Ты завершил игру, сохранений нет. Бывай')
        break

    else:
        print('Нет такого пункта в меню')
    
    print('Вот тебе меню игры:\n\nпродолжить игру\nокно персонажа\nинвентарь\nвыйти из игры')
