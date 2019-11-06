#**************************************************************************
#2-10
#**************************************************************************

#==========================================================================
#region インポート
#==========================================================================

import random
import sys
import math
#endregion


#==========================================================================
#region 変数、リスト、辞書定義
#==========================================================================
data01 = [['見','貝'],['土','士'],['眠','眼']]
data02 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
data03 = ['Ａ','Ｂ','Ｃ','Ｄ','Ｅ','Ｆ','Ｇ','Ｈ','Ｉ','Ｊ','Ｋ','Ｌ','Ｍ','Ｎ','Ｏ','Ｐ','Ｑ','Ｒ','Ｓ','Ｔ','Ｕ','Ｖ','Ｗ','Ｘ','Ｙ','Ｚ','']
level = '1'
row = 4
col = 24
dic01 = {0:'１｜',1:'２｜',2:'３｜',3:'４｜',4:'５｜',5:'６｜',6:'７｜',7:'８｜'}
dic02 = {}
for i in range(col):
    numbers = []
    for j in range(row):
        if i == 0:
            if j == 0:
                numbers.append(j)
            else:
                numbers.append(j * col)
        else:
            numbers.append((j + i ) * col - (row * i))
    dic02[data02[i]] = numbers

int_randam = random.randint(0,2)
mistake_number = random.randint(0,row + col -1)

#endregion

#==========================================================================
#region メッセージ定義
#==========================================================================
message_01 = '違う漢字の番号(例:A1)を入力してください'
message_02 = 'レベル:'
message_03 = '(例:A1)'
message_04 = 'デバッグ:choice = '
#message_05
for i in range(col):
    if i == 0:
        message_05 ='／｜' + data03[i]
    else:
        message_05 += data03[i]
#message_06
message_06 = 'ーー'
for i in range(col):
    message_06 += 'ー'
message_07 = '不正な値です'
message_08 = '警告終了'
message_09 = 'デバッグ:input_number = '
message_10 = 'デバッグ:mistake_number = '
message_11 = '正解！'
message_12 = '不正解！'
message_13 = '正解は '

#endregion

#==========================================================================
#region 関数定義
#==========================================================================

#=====================================
#スタートメッセージ出力
#=====================================
def start_message():
    print(message_01)

#=====================================
#レベル出力
#=====================================
def section_message():
    print(message_02 + level)
    print(message_10 + str(mistake_number))

#=====================================
#クイズ出力
#=====================================
def view_question():
    question_word = data01[int_randam]
    print(question_word)
    print(message_05)
    print(message_06)

    #変数
    i = 0
    j = 0
    k = 0
    question_words = ''
    
    while i < row:
        while j < col:
            if k % col == 0:
                question_words += dic01[i]

            if mistake_number == k:
                question_words += question_word[1]
            else:
                question_words += question_word[0]
            j += 1
            k += 1
        print(question_words)
        question_words = ''
        i += 1
        j = 0

#=====================================
#入力文字列変換(str to int)
#=====================================
def change_input_number(input_str):
    
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

#=====================================
#入力文字列変換(int to str)
#=====================================
def change_string(number):
    
    strABC = data02[number % col]
    int123 = math.floor(number/col) + 1
    return strABC + str(int123) 

#=====================================
#正誤判定
#=====================================
def is_correct_number(mistake_number,input_number):
    if mistake_number == input_number:
        return True
    else:
        return False

#=====================================
#正誤発表
#=====================================
def view_result(is_currect,mistake_numbe):
    if is_currect == True:
        print(message_11)
    else:
        print(message_12)
        answer = change_string(mistake_number)
        print(message_13 + answer)

#=====================================
#クイズゲーム
#=====================================
def play():
    section_message()
    view_question()
    choice = input(message_03)
    input_number = change_input_number(choice)
    print(message_04 + choice)
    print(message_09 + str(input_number))
    is_currect = is_correct_number(mistake_number,input_number)
    view_result(is_currect,mistake_number)
    
#=====================================
#エラーハンドリング（仮）
#=====================================

#警告終了
def alert_end():
    print(message_08)
    sys.exit(0)

#endregion

#==========================================================================
#region クイズ処理
#==========================================================================
start_message()
play()

#endregion
