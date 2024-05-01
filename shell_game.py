from classe import Classes
import random

class Shell():
    def __init__(self, gold):
        self.gold = gold

    def game(self):
        print('So we playing shell game? Okey')  
        bet = int(input(f'How much gold would you like to bet? You have {self.gold} gold\n'))
        while bet <= self.gold:
            print('Okey so we have 3 cup 1, 2 and 3 under 1 we have gold and under rest nothing')
            print('Innkeeper start mix cups and now your turn to choose cup')
            cups = [0, 0, 1]
            random.shuffle(cups)
            print('[0, 1, 2]')
            cup_select = int(input('Choose cup: '))
            if cup_select == 0 or cup_select == 1 or cup_select == 2:
                self.gold -= bet
                if cups[cup_select] == 1:
                    self.gold += 2*bet
                    print(f'Congratulation you win this time now you have {self.gold} gold')
                else:
                    print('Not this time Innkeeper win')
                bet_replay = int(input('Do you want to play again?\n1 - Tak\n2 - Nie\n'))
                if bet_replay == 1:
                    print('*Innkeeper have a big smile on his face*')
                    bet = int(input(f'How much gold would you like to bet? You have {self.gold} gold'))
                else:
                    print('Bye Bye see you next time dont forget about money')
                    break
            else:
                pass
        if bet > self.gold:
            print('Sorry but you do not have enough gold')