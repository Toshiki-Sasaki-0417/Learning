#**************************************************************************
#06-15
#**************************************************************************

#=====================================
#インポート
#=====================================
import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np
import random
import sys

#=====================================
#変数宣言
#=====================================
card_images = []
cards = []
players = []

#=====================================
#クラス定義
#=====================================
class Card:
    def __init__(self,mark,display_name,number,image):
        self.mark = mark
        self.display_name = display_name
        self.number = number
        self.image = image
        self.deal = False

class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.total_number = 0

class Human(Player):
    def __init__(self):
        super().__init__('自分')
        
class Computer(Player):
    def __init__(self):
        super().__init__('コンピューター')

#=====================================
#関数定義
#=====================================
def load_image():
    image_name = 'cards.jpg'
    vsplit_number = 4
    hsplit_number = 13
  
#    if not os.path.isfile(image_name):
    response = requests.get('http://3156.bz/techgym/cards.jpg', allow_redirects=False)
    with open(image_name, 'wb') as image:
        image.write(response.content)
   
    img = cv.imread('./'+image_name)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
 
    h, w = img.shape[:2]
    crop_img = img[:h // vsplit_number * vsplit_number, :w // hsplit_number * hsplit_number]
  
    card_images.clear()
    for h_image in np.vsplit(crop_img, vsplit_number):
        for v_image in np.hsplit(h_image, hsplit_number):
            card_images.append(v_image)

def create_cards():
    marks = ['ハート', 'スペード', 'ダイヤ', 'クローバー']
    display_names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for i,mark in enumerate(marks):
        for j in range(13):
            cards.append( Card(mark,display_names[j],numbers[j],card_images[i * len(numbers) + j] ))

def show_cards(a_cards):
    for i,card in enumerate(a_cards):
        print(card.mark + card.display_name)
        plt.subplot(1,6,i+1)
        plt.axis("off")
        plt.imshow(card.image)
    plt.show()

def deal_card(a_player):
    deal_cards = list(filter(lambda n: n.deal == False, cards))
    if len(deal_cards) == 0:
        print('カードないです。')
        sys.exit(1)

    deal_card = random.choice(deal_cards)
    deal_card.deal = True

    a_player.cards.append(deal_card)
    a_player.total_number += deal_card.number


def win():
    print('勝ち')

def lose():
    print('負け')

def choice():
    choice = ''
    choice = str(input('ヒット[1] or スタンド[2]'))

    while enable_choice(choice) == False:
        choice = str(input('ヒット[1] or スタンド[2]'))
    
    return int(choice)

def enable_choice(a_choice):
    if a_choice != '1' and a_choice != '2':
        return False
    else:
        return True

def play_once():

    deal_card(players[0])
    deal_card(players[1])
    deal_card(players[0])
    show_cards(players[0].cards)

    if is_blackjack() == True:
        win()
    else:
        if is_burst() == True:
            lose()
            sys.exit(1)
        else:
            if choice() == True:
                hit()
            else:
                stand()
    
def is_blackjack():
    if players[0].total_number == 21:
        return True
    else:
        return False

def is_burst():
    if players[0].total_number > 21:
        return True
    else:
        return False

def hit():
    deal_card(players[0])
    show_cards(players[0].cards)

    if is_blackjack() == True:
        win()
    else:
        if is_burst() == True:
            lose()
            sys.exit(1)
        else:
            if choice() == True:
                hit()
            else:
                stand()

def stand():
    if players[1].total_number <= 17:
        deal_card(players[1])
    else:
        judge()

def judge():
    print('結果')


def play():
    print('デバッグログ：play()')
    load_image()
    create_cards()
    players.append(Human())
    players.append(Computer())

    play_once()

#=====================================
#実行
#=====================================
play()
