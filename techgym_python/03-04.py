#**************************************************************************
#03-03
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

    #チーム定義情報表示
    def info(self):
        print(self.name + ': 攻撃力:' + str(self.attack) + ' / 守備力:' + str(self.defence))

#=====================================
#関数定義
#=====================================

#チーム定義
def create_teams():
    team01 = Team('アタッカーズ', 80, 20)
    team02 = Team('ディフェンダーズ', 30, 70)
    team03 = Team('アベレージーズ', 50, 50)
    #teams.append(team01)
    #teams.append(team02)
    #teams.append(team03)
    teams = [team01,team02,team03]

    print('全チーム情報')
    idx = 1
    for team in teams:
        print(idx)
        team.info()
        idx += 1

#開始
def play():
  print('デバッグログ：play()')
  create_teams()
  

play()
