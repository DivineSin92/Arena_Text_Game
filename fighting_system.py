import random
from classe import Classes

class Fighting():
    def __init__(self, dmg, hp, gold, exp, maxhp, potki, lvl):
        self.dmg = dmg
        self.hp = hp
        self.gold = gold
        self.exp = exp
        self.maxhp = maxhp
        self.potki = potki
        self.lvl = lvl

    def enemy_fight(self, difficulty):
        if difficulty == 1:
            enemy_hp = random.choice((90, 100, 110))
            enemy_dmg = random.choice((10, 20, 30))
        elif difficulty == 2:
            enemy_hp = random.choice((150, 160, 170))
            enemy_dmg = random.choice((40, 50, 60))
        elif difficulty == 'boss':
            enemy_hp = random.choice((100, 150)) * self.lvl
            enemy_dmg = random.choice((40, 50, 60)) * self.lvl
        print(f'Your enemy have {enemy_hp} hp and {enemy_dmg} dmg')
        Fighting.fight(self, difficulty, enemy_hp, enemy_dmg)
        
    def fight(self, difficulty, enemy_hp, enemy_dmg):
        while enemy_hp > 0 and self.hp > 0:
            enemy_hp -= self.dmg
            self.hp -= enemy_dmg
            print(f'Your hp {self.hp} enemy hp {enemy_hp}')
        if enemy_hp <= 0 and self.hp > 0:
            reward_gold = difficulty * random.choice((10, 20, 30))
            reward_exp = difficulty * random.choice((20, 30))
            print(f'You win after defeating your enemy you get {reward_gold} gold and {reward_exp} exp')
            self.gold += reward_gold
            self.exp += reward_exp
            Classes.lvl_up(self)
        else:
            Fighting.healing_or_death_system(self)

    def healing_or_death_system(self):
        if self.potki >= 1:
            print('Potion of immortality save your life')
            self.hp = self.lvl + 5 * 25
            if self.hp > self.maxhp:
                self.hp = self.maxhp
        else:
            print('You have been defeated your enemy steal all your gold')
            self.hp = self.lvl + 5 * 20
            self.gold = 0