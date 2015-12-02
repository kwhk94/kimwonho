__author__ = 'kkk'

from pico2d import*
import game_framework
import battlemap
import title
import map
import json
import random
global dice_num
global font

class Card():
    image=None
    result=None
    def __init__(self):
        if self.image==None:
            self.image=[load_image('png\\card1.png'),
                        load_image('png\\card2.png'),
                        load_image('png\\card3.png'),
                        load_image('png\\card4.png'),
                        load_image('png\\card5.png'),
                        load_image('png\\card6.png'),
                        load_image('png\\card7.png')]
        if self.result==None:
            self.result_road=[load_image('png\\result.png'),
                         load_image('png\\result 2.png'),
                         load_image('png\\result 3.bmp')]
            self.result_wood=[load_image('png\\resultwood1.png'),
                         load_image('png\\resultwood2.png'),
                         load_image('png\\resultwood3.png')]
