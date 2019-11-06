#2-3

import random

#メッセージ定義
message_01 = '違う漢字の番号(例:A1)を入力してください'
message_02 = 'レベル:'
message_03 = '(例:A1)'
message_04 = 'デバッグ:choice = '

#
data = [['貝','貝'],['土','土'],['眼','眼']]
level = '1'
int_randam = random.randint(0,2)
print(int_randam)

#関数定義
def start_message():
    print(message_01)

def section_message():
    print(message_02 + level)

def view_question():
    print(data[int_randam])

def play():
    section_message()
    view_question()
    choice = input(message_03)
    print(message_04 + choice)

start_message()
play()
