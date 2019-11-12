#**************************************************************************
#03-07
#**************************************************************************

import random
import math

#=====================================
#変数定義
#=====================================
teams = []

playing_teams = {'myself':False,'enemy':False}

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
    #
    def get_hit_rate(self):
        return random.randint(10,self.attack)
    
    #
    def get_out_rate(self):
        return random.randint(10,self.defence)

#=====================================
#関数定義
#=====================================

#チーム定義
def create_teams():
    global teams
    team01 = Team('アタッカーズ', 80, 20)
    team02 = Team('ディフェンダーズ', 30, 70)
    team03 = Team('アベレージーズ', 50, 50)
    teams = [team01,team02,team03]

 
#
def show_team():
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
    print(who_team + 'のチームは「' + teams[team_number-1].name + '」です')
    playing_teams[who] = teams[team_number-1]
    return team_number

#
def get_play_inning(inning):
    if inning == 'front':
        front_name = 'myself'
        back_name = 'enemy'
    elif inning == 'back':
        front_name = 'enemy'
        back_name = 'myself'

    hit = playing_teams[front_name].get_hit_rate()
    out = playing_teams[back_name].get_out_rate()
    score = (math.floor((hit - out) / 10))
    if score < 0:
        return 0
    else:
        return score

#開始
def play():
    create_teams()
    show_team()
    choice_team('myself')
    choice_team('enemy')
  
    for i in range(9):
        score_front = get_play_inning('front')
        score_back = get_play_inning('back')
        print( str(i+1) + '回表 ' + str(score_front) )
        print( str(i+1) + '回裏 ' + str(score_back) )

play()
