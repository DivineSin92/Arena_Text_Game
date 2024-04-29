class Classes():
    def __init__(self, name, hp, maxhp, dmg, gold, lvl, exp, max_exp, potki):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.dmg = dmg
        self.gold = gold
        self.lvl = lvl
        self.exp = exp
        self.max_exp = max_exp
        self.potki = potki

    def __str__(self) -> str:
        return f"class {self.name}\nhp = {self.hp}\nmaxhp = {self.maxhp}\ndmg = {self.dmg}\ngold = {self.gold}\nlvl = {self.lvl}\nexp = {self.exp}\nmax_exp = {self.max_exp}\npotki = {self.potki}"

    def class_select_f(self):
        while self != 1 or self != 2 or self != 3:
            if self == 1:
                character = class1
                print(f'You became {character.name}')
                return character
            elif self == 2:
                character = class2
                print(f'You became {character.name}')
                return character
            elif self == 3:
                character = class3
                print(f'You became {character.name}')
                return character
            else:
                raise OverflowError('Sorry but choose existing class')

    def lvl_up(self):
        if self.exp >= self.max_exp:
            self.lvl += 1
            self.exp -= self.max_exp
            self.max_exp += 50
            self.maxhp += 50
            self.hp = self.maxhp
            self.dmg += 5
            print(f'Congratulation you reach {self.lvl} lvl! Good Job!')

class1 = Classes("Warrrior", 200, 250, 50, 0, 1, 0, 100, 0)
class2 = Classes("Mage", 100, 150, 50, 0, 1, 0, 100, 3)
class3 = Classes("Thief", 100, 150, 50, 350, 1, 0, 100, 0)
