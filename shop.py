import items

class Shop():
    def __init__(self, gold, maxhp, dmg):
        self.gold = gold
        self.maxhp = maxhp
        self.dmg = dmg

    def select_shop(self):
        print('Welcom in shop you can buy here new weapon, armor or get a few potions')
        print('1 - Weapons\n2 - Armors\n3 - Potions')
        shop = int(input('What you searching for?\n'))
        if shop == 1:
            Shop.weapon_shop(self)
        elif shop == 2:
            Shop.armor_shop(self)
            
    def weapon_shop(self):
        print('╔' + 5 * '═' + '╦' + 21 * '═' + '╦' + 7 * '═' + '╦' + 8 * '═' + '╗')
        print('║' + ' id  ' + '║' + '        name         ' + '║' + '  dmg  ' + '║' + '  price ' + '║')
        print('╠' + 5 * '═' + '╬' + 21 * '═' + '╬' + 7 * '═' + '╬' + 8 * '═' + '╣')
        print(items.sword1)
        print(items.sword2)
        print(items.sword3)
        print(items.sword4)
        print('╚' + 5 * '═' + '╩' + 21 * '═' + '╩' + 7 * '═' + '╩' + 8 * '═' + '╝')
        select = int(input('What do you need?'))
        if select == 1:
            item = items.sword1
        elif select == 2:
            item = items.sword2
        elif select == 3:
            item = items.sword3
        elif select == 4:
            item = items.sword4
        else:
            print('sorry do not have this item yet')
            item = None
        if item != None:
            Shop.checking_money(self, item)

    def armor_shop(self):
            print('╔' + 5 * '═' + '╦' + 34 * '═' + '╦' + 7 * '═' + '╦' + 8 * '═' + '╗')
            print('║' + ' id  ' + '║' + '              name                ' + '║' + '  hp   ' + '║' + '  price ' + '║')
            print('╠' + 5 * '═' + '╬' + 34 * '═' + '╬' + 7 * '═' + '╬' + 8 * '═' + '╣')
            print(items.armor1)
            print(items.armor2)
            print(items.armor3)
            print(items.armor4)
            print('╚' + 5 * '═' + '╩' + 34 * '═' + '╩' + 7 * '═' + '╩' + 8 * '═' + '╝')
            select = int(input('What do you need?'))
            if select == 1:
                item = items.armor1
            elif select == 2:
                item = items.armor2
            elif select == 3:
                item = items.armor3
            elif select == 4:
                item = items.armor4
            else:
                print('sorry do not have this item yet')
                item = None
            if item != None:
                Shop.checking_money(self, item)

    def checking_money(self, item):
        if self.gold >= item.price:
                self.gold -= item.price
                self.maxhp += item.zhp
                self.dmg += item.bdmg
                print('Here you are it is your item ;)')
        else:
            print('Sorry you do not have enough gold')