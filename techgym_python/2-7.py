#2-6

import random
import sys

#メッセージ定義
message_01 = '違う漢字の番号(例:A1)を入力してください'
message_02 = 'レベル:'
message_03 = '(例:A1)'
message_04 = 'デバッグ:choice = '
message_05 = '／｜ＡＢＣ'
message_06 = 'ーーーーー'
message_07 = '不正な値です'
message_08 = '警告終了'
message_09 = 'デバッグ:input_number = '

#
data = [['見','貝'],['土','士'],['眠','眼']]
level = '1'
dic01 = {0:'１｜',1:'２｜',2:'３｜'}
dic02 = {'A':[0,3,6],'B':[1,4,7],'C':[2,5,8]}


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

def change_input_nuimber(input_str):
    
    #入力内容の分割
    list_input_str = list(input_str)
    
    #入力内容チェック（文字数のみ）
    if len(list_input_str) != 2:
        print(message_07)
        alert_end()
    else:
        strABC = list_input_str[0]
        int123 = int(list_input_str[1])
        num_list = dic02[strABC]
        return num_list[int123 -1]

def play():
    section_message()
    view_question()
    choice = input(message_03)
    input_number = change_input_nuimber(choice)
    print(message_04 + choice)
    print(message_09 + str(input_number))

def alert_end():
    print(message_08)
    sys.exit(0)

start_message()
play()
