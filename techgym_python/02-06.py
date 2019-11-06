#2-6

import random

#メッセージ定義
message_01 = '違う漢字の番号(例:A1)を入力してください'
message_02 = 'レベル:'
message_03 = '(例:A1)'
message_04 = 'デバッグ:choice = '
message_05 = '／｜ＡＢＣ'
message_06 = 'ーーーーー'

#
data = [['見','貝'],['土','士'],['眠','眼']]
level = '1'
dic01 = {0:'１｜',1:'２｜',2:'３｜'}
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
    print(message_05)
    print(message_06)


    #変数
    i = 0
    j = 0
    k = 0
    question_words = ''
    randam_idx = random.randint(0,8)

    while i < 3:
        while j < 3:
            if k % 3 == 0:
                question_words += dic01[i]

            if randam_idx == k:
                question_words += question_word[1]
            else:
                question_words += question_word[0]
            j += 1
            k += 1
        print(question_words)
        question_words = ''
        i += 1
        j = 0

def play():
    section_message()
    view_question()
    choice = input(message_03)
    print(message_04 + choice)

start_message()
play()
