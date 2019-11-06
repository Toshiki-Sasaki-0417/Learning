#2-4

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
    question_word = data[int_randam]
    print(question_word)
    
    #ループ用変数初期化
    i = 0
    j = 0
    question_words = ''

    while i < 3:
        i += 1
        while j < 3:
            question_words += question_word[0]
            j += 1
        print(question_words)

def play():
    section_message()
    view_question()
    choice = input(message_03)
    print(message_04 + choice)

start_message()
play()
