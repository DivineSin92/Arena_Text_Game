class Weapon():
    def __init__(self, id, name, bdmg, zhp, price):
        self.id = id
        self.name = name
        self.bdmg = bdmg
        self.zhp = zhp
        self.price = price
    def __str__(self):
        return f"║  {self.id:1d}  ║  {self.name:17s}  ║  {self.bdmg:3d}  ║  {self.price:4d}  ║"

sword1 = Weapon(1, 'Żelazny miecz', 20, 0, 100)
sword2 = Weapon(2, 'Epicki miecz', 40, 0, 200)
sword3 = Weapon(3, 'Legendarny miecz', 50, 0, 400)
sword4 = Weapon(4, 'Pożeracz światów', 200, 0, 999)

class Armor():
    def __init__(self, id, name, zhp, bdmg, price):
        self.id = id
        self.name = name
        self.zhp = zhp
        self.bdmg = bdmg
        self.price = price
    def __str__(self):
        return f'║  {self.id:1d}  ║  {self.name:30s}  ║  {self.zhp:3d}  ║  {self.price:4d}  ║'

armor1 = Armor(1, 'Żelazna zbroja', 25, 0, 100)
armor2 = Armor(2, 'Epicka zbroja', 50, 0, 200)
armor3 = Armor(3, 'Legendarna zbroja', 100, 0, 400)
armor4 = Armor(4, 'Zbroja niszczyciela światów', 300, 0, 999)