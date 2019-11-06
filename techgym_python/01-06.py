#1-6

#インポート
import random

#リスト定義
hands = ['グー','チョキ','パー']
results = {'win':'勝ち','lose':'負け','draw':'あいこ'}

#関数定義
def start_message():
    print('じゃんけんスタート')

def get_my_hand():  
    print('自分の手を入力してください')

    #変数初期化
    input_message = ''
    idx = 0
    
    for i in hands:
        input_message += str(idx) + ':' + i
        if idx < 2:
            input_message += ','
        idx += 1

    return int(input(input_message))

def get_you_hand():  
    return random.randint(0,2)

def get_hand_name(hand_number):
    if hand_number == 0:
        return 'グー'
    elif hand_number == 1:
        return 'チョキ'
    else:
        return 'パー'

def view_hand(my_hand,you_hand):
    print('自分の手は' + get_hand_name(my_hand))
    print('相手の手は' + get_hand_name(you_hand))

def get_result(hand_diff):
    if hand_diff == 0:
      return('draw')
    elif hand_diff in (-1,2):
      return('win')
    else:
      return('lose')

def view_result(result):  
    print(results[result])



#じゃんけん処理
my_hand = get_my_hand()
you_hand = get_you_hand()
hand_diff = my_hand - you_hand

view_hand(my_hand,you_hand)
result = get_result(hand_diff)
view_result(result)
