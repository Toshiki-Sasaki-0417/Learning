#**************************************************************************
#03-02
#**************************************************************************

import random

#=====================================
#変数定義
#=====================================
global teams
teams = []

#=====================================
#クラス定義
#=====================================
class Team:
  def __init__(self, name, attack, defence):
    self.name = name
    self.attack = attack
    self.defence = defence

#=====================================
#関数定義
#=====================================
def create_teams():
    team01 = Team('アタッカーズ', 80, 20)
    team02 = Team('ディフェンダーズ', 30, 70)
    team03 = Team('アベレージーズ', 50, 50)
    teams.append(team01)
    teams.append(team02)
    teams.append(team03)



def play():
  print('デバッグログ：play()')
  create_teams()

play()
