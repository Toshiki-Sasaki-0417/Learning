#1-1
import random

print('じゃんけんスタート')

print('自分の手を入力してください')
my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
you_hand = random.randint(0,2)

if my_hand == 0:
  if you_hand == 0:
    print('あいこ')
  elif you_hand == 1:
    print('勝ち')
  else:
    print('負け')
elif my_hand == 1:
  if you_hand == 0:
    print('負け')
  elif you_hand == 1:
    print('あいこ')
  else:
    print('勝ち')
else:
  if you_hand == 0:
    print('勝ち')
  elif you_hand == 1:
    print('負け')
  else:
    print('あいこ')
