#**************************************************************************
#04-04
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

class Human(Player):
    def __init__(self, name,coin):
        super().__init__(name,coin)

#=====================================
#関数定義
#=====================================
def play():
    
    Human01 = Human('MY',500)
    print('デバッグログ：play()')

#=====================================
#本編
#=====================================
play()





