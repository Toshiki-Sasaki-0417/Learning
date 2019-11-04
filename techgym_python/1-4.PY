#1-4

#インポート
import random

#関数定義
def start_message():
  print('じゃんけんスタート')

def get_my_hand():  
  print('自分の手を入力してください')
  return int(input('0:グー, 1:チョキ, 2:パー'))

def get_you_hand():  
  return random.randint(0,2)

def view_result(x):  
  if x == 0:
    print('あいこ')
  elif x in (-1,2):
    print('勝ち')
  else:
    print('負け')

#じゃんけん処理
hand_diff = get_my_hand() - get_you_hand()
view_result(hand_diff)
