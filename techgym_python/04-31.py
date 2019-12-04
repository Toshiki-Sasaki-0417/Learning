#**************************************************************************
#04-31
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
cells = []

#=====================================
#クラス定義
#=====================================
class Player:
    def __init__(self, name,coin):
        self.name = name
        self.coin = coin
        self.bets = {}
        reset_table()

        for cell in table:
            self.bets.update({cell.name: 0})
    
    def set_bet_coin(self,bet_coin):
        self.coin += -(int(bet_coin))
    
    def reset_table(self):
        for cell in table:
            self.bets.update({cell.name: 0})

class Human(Player):
    def __init__(self, name,coin):
        super().__init__(name,coin)
    
    #BET
    def bet(self):
        if self.coin < 99:
            max_bet_coin = self.coin
        else:
            max_bet_coin = 99

        bet_message = '何枚BETしますか？：（1-' + str(max_bet_coin) + '）'
        bet_message02 = 'どこにBETしますか？：（R,B,1-8）'
        bet_coin = str(input(bet_message))
        while not self.enable_bet_coin(bet_coin,max_bet_coin):
            bet_coin = str(input(bet_message))
        
        self.set_bet_coin(bet_coin)

        bet_cell = str(input(bet_message02))
        while not self.enable_bet_cell(bet_cell):
            bet_cell = str(input(bet_message02))
        self.bets[bet_cell] = bet_coin
        print(self.name + 'は' + str(bet_coin) + 'コインを' + bet_cell + 'にBETしました。')
    
    #CHECK
    def enable_bet_coin(self,string,max_bet_coin):
        if str.isdecimal(string) == True:
            if 1<= int(string) <= max_bet_coin:
                return True
            else:
                return False
        else:
             return False
    
    #CHECK
    def enable_bet_cell(self,string):
        if str.isdecimal(string) == True:
            if 1<= int(string) <= 8:
                return True
            else:
                return False
        else:
            if string == 'R' or string == 'B':
                return True
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

        bet_cell_num = random.randint(0,len(cells)-1)
        bet_cell = cells[bet_cell_num]
        self.bets[bet_cell] = bet_coin
        print(self.name + 'は' + str(bet_coin) + 'コインを' + bet_cell + 'にBETしました。')
    
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
    bar = green_bar()
    row = bar + '_____' + bar
    for Player in players:
        row += Player.name + bar
    print(row)

    while num < row_cnt:
        row = color(table[num].color,table[num].name + '(x' + str(table[num].rate) + ')')
        row = bar + row + bar
        for player in players:
            row += str(player.bets[table[num].name]).zfill(2) + bar
        print(row)
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
def set_cells():
    global cells
    for cell in table:  
        cells.append(cell.name)

#
def check_hit():
    hit = cells[random.randint(0,9)]
    print('選ばれたのは' + '「' + hit +'」')

    for player in players:
        num = 0
        for cell in cells:
            if player.bets[cell] != 0 and hit == cell:
               win_player(player,num)
            num += 1

#
def win_player(player,hit_cell_number):
    cell = table[hit_cell_number].name
    rate = table[hit_cell_number].rate
    
    for i in cells:
        if player.bets[i] != 0:
            bet = int(player.bets[i])

    reward = rate * bet
    player.coin += reward
    print(player.name + 'は当たり' + str(reward) + 'コインを獲得しました。')

#
def show_coin():
    message = '[持ちコイン]'
    for player in players:
        message += player.name + ':' + str(player.coin) + '/'
    print(message)

#
def reset_table():
  for player in players:
    player.reset_table()

#
def initialize():
    create_table()
    create_players()
    set_cells()
    
#
def play_once():
    reset_table()
    bet_players()
    show_table()
    check_hit()
    show_coin()

#
def is_game_end():
    for Player in players:
        if Player.coin <= 0:
            return True
            exit
        else:
            return False
#
def bet_players():
    for player in players:
        player.bet()
    
#
def play():
    initialize()
    play_once()

#
def game_end():
    for player in players:
        if player.coin <= 0:
            print(player.name + 'のコインがなくなっためゲームを終了します。')


#=====================================
#本編
#=====================================
play()

while is_game_end() == False:
    play_once()
else:
    game_end()