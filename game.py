from classe import Classes
from dialogs import Texts
from shell_game import Shell
from shop import Shop
from fighting_system import Fighting

#-----------------------------------------------------------------#
Texts.start_text()
class_select = int(input('Select your class: '))
character = Classes.class_select_f(class_select)

while character.hp>0:
    #-------------------------Path-------------------------#
    Texts.village_text()
    road_to = int(input('Where are we going?\n'))

    #-------------------------Stats-------------------------#
    if road_to == 1:
      Texts.stats(character)

    #-------------------------Tawern-------------------------#
    elif road_to == 2:
      Texts.tavern(character)

    #-------------------------easy-fight-------------------------#
    elif road_to == 3:
      #Fighting.enemy_fight(character, 1)
      pass

    #-------------------------hard-fight-------------------------#
    elif road_to == 4:
      #Fighting.enemy_fight(character, 2)
      pass

    #-------------------------boss-fight-------------------------#
    elif road_to == 5:
      #Fighting.enemy_fight(character, 'boss')
      pass

    #-------------------------shell-game-------------------------#
    elif road_to == 6:
      #Shell.game(character)
      pass

    #-------------------------shopp-------------------------#
    elif road_to == 7:
      #Shop.select_shop(character)
      pass

    #-------------------------Save-------------------------#
    elif road_to == 8:
      pass

    #-------------------------Load-------------------------#
    elif road_to == 9:
      pass

    #-------------------------Exit-------------------------#
    elif road_to == 10:
      print(':( Good Bye')
      break

    #-------------------------Wrong-way-------------------------#
    else:
      print('Choose something from list!')
