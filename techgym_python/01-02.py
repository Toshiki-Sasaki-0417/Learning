#1-2

import random

print('じゃんけんスタート')

print('自分の手を入力してください')
my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
you_hand = random.randint(0,2)
diff_hand = my_hand - you_hand

if diff_hand == 0:
  print('あいこ')
elif diff_hand in (-1,2):
  print('勝ち')
else:
  print('負け')