#**************************************************************************
#04-08
#**************************************************************************

#=====================================
#インポート
#=====================================
import random

#=====================================
#クラス定義
#=====================================
class Player:
    def __init__(self, name,coin):
        self.name = name
        self.coin = coin
    
    #INFO
    def info(self):
        print(self.name + '：' + str(self.coin))
    
    def set_bet_coin(self,bet_coin):
        self.coin += -(int(bet_coin))


class Human(Player):
    def __init__(self, name,coin):
        super().__init__(name,coin)
    
    #BET
    def bet(self):
        bet_message = '何枚BETしますか？：（1-99）'
        
        bet_coin = str(input(bet_message))
        while not self.enable_bet_coin(bet_coin):
            bet_coin = str(input(bet_message))
        
        self.set_bet_coin(bet_coin)

        print('デバッグログ：' + str(bet_coin))
    
    #CHECK
    def enable_bet_coin(self,string):
        if str.isdecimal(string) == True:
            if 1<= int(string) <= 99:
                return True
            else:
                return False
        else:
             return False

#=====================================
#関数定義
#=====================================

#
def play():
    
    print('デバッグログ：play()')
    Human01 = Human('MY',500)
    Human01.info()
    Human01.bet()
    Human01.info()

#=====================================
#本編
#=====================================
play()






