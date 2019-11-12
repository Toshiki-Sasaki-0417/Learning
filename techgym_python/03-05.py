#**************************************************************************
#03-03
#**************************************************************************

import random

#=====================================
#変数定義
#=====================================
global teams
teams = []

playing_teams = {1:'アタッカーズ',2:'ディフェンダーズ',3:'アベレージーズ'}

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
    teams = [team01,team02,team03]

    print('全チーム情報')
    idx = 1
    for team in teams:
        print(idx)
        team.info()
        idx += 1

#
def choice_team(who):
    who_team = ''
    if who == 'myself':
        who_team = '自分'
    else:
        who_team = '相手'
    team_number = int(input(who_team + 'のチームを選択してください（1~3）'))
    print(who_team + 'のチームは「' + playing_teams[team_number] + '」です')

#開始
def play():
  create_teams()
  choice_team('myself')
  choice_team('enemy')

play()
