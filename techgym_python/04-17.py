#**************************************************************************
#04-17
#**************************************************************************

#=====================================
#インポート
#=====================================
import random


#=====================================
#変数宣言
#=====================================
players = []
table = []

#=====================================
#クラス定義
#=====================================
class Player:
    def __init__(self, name,coin):
        self.name = name
        self.coin = coin
        for cell in table:
            self.bets.update({cell.name: 0})

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

class Computer(Player):
    def __init__(self, name,coin):
        super().__init__(name,coin)
    
    #BET
    def bet(self):

        if self.coin < 99:
            bet_coin = random.randint(1,self.coin)
        else:
            bet_coin = random.randint(1,99)
             
        self.set_bet_coin(bet_coin)

        print('デバッグログ：' + str(bet_coin))
    
class Cell:
    def __init__(self, name,rate,color):
        self.name = name
        self.rate = rate
        self.color = color

class ColorBase:
  BLACK = '\033[30m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  END = '\033[0m'

#=====================================
#関数定義
#=====================================

#
def create_players():
    global players 
    Human01 = Human('MY',500)
    Computer01 = Computer('C1',500)
    Computer02 = Computer('C2',500)
    Computer03 = Computer('C3',500)
    players = [Human01,Computer01,Computer02,Computer03]

#
def show_players():

    for player in players:
        player.info()

#
def create_table():
    global table
    table.append(Cell('R',8,'red'))
    table.append(Cell('B',8,'black'))
    table.append(Cell('1',2,'red'))
    table.append(Cell('2',2,'black'))
    table.append(Cell('3',2,'red'))
    table.append(Cell('4',2,'black'))
    table.append(Cell('5',2,'red'))
    table.append(Cell('6',2,'black'))
    table.append(Cell('7',2,'red'))
    table.append(Cell('8',2,'black'))

#
def show_table():
    
    row_cnt = len(table)
    num = 0
    while num < row_cnt:
        result = color(table[num].color,table[num].name + '(x' + str(table[num].rate) + ')')
        bar = green_bar()
        print(bar + result + bar)
        num += 1

#
def color(color_name,string):
    if color_name == 'red':
        return ColorBase.RED + string + ColorBase.END
    elif color_name == 'black':
        return ColorBase.BLACK + string + ColorBase.END

#
def green_bar():
    return ColorBase.GREEN + '|' + ColorBase.END

#
def play():
    
    create_players()
    print('デバッグログ：play()')
    show_players()
    
    for player in players:
        player.info()
        player.bet()
        player.info()
    
    create_table()
    show_table()

#=====================================
#本編
#=====================================
play()






