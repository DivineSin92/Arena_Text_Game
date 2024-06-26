import random, time
from save_with_db import Save

class Texts():
    def start_text():
        start = '''

            ░█████╗░██████╗░███████╗███╗░░██╗░█████╗░
            ██╔══██╗██╔══██╗██╔════╝████╗░██║██╔══██╗
            ███████║██████╔╝█████╗░░██╔██╗██║███████║
            ██╔══██║██╔══██╗██╔══╝░░██║╚████║██╔══██║
            ██║░░██║██║░░██║███████╗██║░╚███║██║░░██║
            ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝
    Welcom in the world when you can just fight vs enemies
    Now you can choose your class but do it carefully
    You can be: 

    (1)Strong warrior with more hp
    (2)Clever alchemist with potions at start
    (3)Sneaky thief with more gold at start

    Choose wisely'''
        print(start)

    def village_text():
        village = """

    1  - Stats
    2  - Rest in Tawern
    3  - Fight vs week enemy
    4  - Fight vs strong enemy
    5  - Boss fight
    6  - Shell game
    7  - Shop
    8  - 
    9  - 
    10 - Exit

        """
        print(village)
        time.sleep(1)

    def stats(self):
        stat = f'''
        ╔═════════════╦═══════════╗
        ║    name     ║   amount  ║
        ╠═════════════╬═══════════╣
        ║     hp      ║  {self.hp:5d}    ║
        ║    maxhp    ║  {self.maxhp:5d}    ║
        ║     dmg     ║  {self.dmg:5d}    ║
        ║    gold     ║  {self.gold:5d}    ║
        ║     lvl     ║  {self.lvl:5d}    ║
        ║     exp     ║  {self.exp:5d}    ║
        ║   max exp   ║  {self.max_exp:5d}    ║
        ║    potki    ║  {self.potki:5d}    ║
        ╚═════════════╩═══════════╝
        '''
        print(stat)

    def tavern(self):
        tawern_cost = self.lvl*20 + random.choice((10, 20, 30))
        if self.gold >= tawern_cost:
            print('So we go sleep. Good Night!')
            print(f'Inkeeper thanks you for {tawern_cost} gold')
            self.gold -= tawern_cost
            self.hp = self.maxhp
        else:
            print('Sorry but you do not have enough gold')

    def character_menu(character, name):
        menu = '''
    1   -   Check character list
    2   -   Save Progress
    3   -   Loading Save
    '''
        print(menu)
        menu_option = int(input('Select what to do: '))
        if menu_option == 1:
            Save.check_character()
        elif menu_option == 2:
            Save.save_progress(character, name)
        elif menu_option == 3:
            Save.check_character()
            loadin_name = input('What is your loading character name? ')
            Save.loading_character(character, loadin_name)
        else:
            print('Dont have this option')