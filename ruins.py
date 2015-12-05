__author__ = 'kkk'
from pico2d import*
import game_framework
import battlemap
import title
import json
import random
import map
global dice_num
global font
import gameover
import mapclass
from Tileclass import Tile as Tile
from Tileclass import Move as Move
from cardclass import Card as Card
from statclass import Stat_downside as Stat

def handle_events():
    global running,xpos,ypos,actionnumber
    global map,move,tile,turnnumber,cardnumber
    global stat,mouse_x,mouse_y,statonoff,itemnumber
    global pausenum,dice_num,tiletype,turntype
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                if turntype==3 :
                    turntype=4
                elif turntype==4:
                    game_framework.pop_state()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_p):
                if pausenum==1: pausenum=0
                elif pausenum==0:pausenum=1
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_o):
                 print(battlemap.dice_num)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_i):
                 stat.onoff= not stat.onoff
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_q):
                 game_framework.pop_state()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_KP_MINUS):
                if turntype==3 and itemnumber>0:
                    itemnumber-=1
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_KP_PLUS):
                if turntype==3 and itemnumber<map.chracter.gold:
                    itemnumber+=1
            if (event.type,event.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
                     mouse_x,mouse_y=event.x,599-event.y
                     if turntype==1 :
                         actionnumber=click_card()


def result(num):
    global turntype,turnnumber,chracter
    map.turnnumber+=1
    if num>=0 and num<(map.chracter.luk*3)+2:
            if map.chracter.str<12:
                map.chracter.str+=1
    elif num>=(map.chracter.luk*3)+2 and num<((map.chracter.luk*3)+2)*2:
            if map.chracter.df<5:
                map.chracter.df+=1
    elif num<((map.chracter.luk*3)+2)*2+5 and num<((map.chracter.luk*3)+2)*2+10:
         if map.chracter.str>1:
                map.chracter.str-=1
    elif num<((map.chracter.luk*3)+2)*2+10 and num<((map.chracter.luk*3)+2)*2+15:
            if map.chracter.df>1:
                map.chracter.df-=1
    else :
           pass


def click_card():
    global mouse_x,mouse_y
    global turntype
    num=[0,0,0]
    for i in range(3) :
        num[i]=random.randint(0,100)
    if mouse_x>50 and mouse_x<250 and mouse_y>200 and mouse_y<500 :
        mouse_x,mouse_y=-100,-100
        turntype=3
        print(num[0])
        return num[0]
    elif mouse_x>300 and mouse_x<500 and mouse_y>200 and mouse_y<500 :
        mouse_x,mouse_y=-100,-100
        turntype=3
        print(num[1])
        return num[1]
    elif mouse_x>550 and mouse_x<750 and mouse_y>200 and mouse_y<500 :
        mouse_x,mouse_y=-100,-100
        turntype=3
        print(num[2])
        return num[2]




def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time



def drawcard(num):
    global cardnumber
    global turntype
    road,wood=1,8
    if turntype==1:
        stat.onoff=1
        card.image[cardnumber%7].clip_draw(0,0,200,300,150,350) #draw_rectangle(50,200,250,500)
        card.image[(cardnumber+1)%7].clip_draw(0,0,200,300,400,350)#draw_rectangle(300,200,500,500)
        card.image[(cardnumber+2)%7].clip_draw(0,0,200,300,650,350)#draw_rectangle(550,200,750,500)
    elif turntype==3:
            if num>=0 and num<(map.chracter.luk*3)+2:
                card.ruins.clip_draw(0,0,266,399,150,350)
                font.draw(90,380,"새로운 무기를",color=(150,350,0))
                font.draw(90,350,"얻었다. (힘+1)",color=(150,350,0))
                font.draw(90,320,"(최대 12)",color=(150,350,0))
            elif num>=(map.chracter.luk*3)+2 and num<((map.chracter.luk*3)+2)*2:
                card.ruins.clip_draw(0,0,266,399,150,350)
                font.draw(90,380,"새로운 방어구를",color=(150,350,0))
                font.draw(90,350,"얻었다. (방어+1)",color=(150,350,0))
                font.draw(90,320,"(최대 5)",color=(150,350,0))
            elif num<((map.chracter.luk*3)+2)*2+5 and num<((map.chracter.luk*3)+2)*2+10:
                card.ruins.clip_draw(0,0,266,399,150,350)
                font.draw(90,380,"무기가 오래되어",color=(150,350,0))
                font.draw(90,350,"부식되었다. (방어-1)",color=(150,350,0))
                font.draw(90,320,"(최소 1)",color=(150,350,0))
            elif num<((map.chracter.luk*3)+2)*2+10 and num<((map.chracter.luk*3)+2)*2+15:
                card.ruins.clip_draw(0,0,266,399,150,350)
                font.draw(90,380,"떨어지는 바위에 ",color=(150,350,0))
                font.draw(90,350,"방어구가 망가졌다",color=(150,350,0))
                font.draw(90,320,"(방어 -1, 최소 1)",color=(150,350,0))
            else:
                card.ruins.clip_draw(0,0,266,399,150,350)
                font.draw(90,380,"발견된 것이",color=(150,350,0))
                font.draw(90,350,"없다",color=(150,350,0))
    if turntype==4:
         result(actionnumber)
         game_framework.pop_state()


def enter():
    global map, move,chracter,tile
    global pausenum,mouse_x,mouse_y,dice_num
    global stat,font,smallfont,bigfont
    global timer,tiletype,turntype,turnnumber
    global current_time,bgm,card, actionnumber
    global xpos,ypos,cardnumber, itemnumber,backpicture
    backpicture=load_image('png\\dungen.jpg')
    itemnumber=0;
    xpos,ypos=0,0
    actionnumber=0
    card=Card()
    cardnumber=random.randint(0,100);
    turntype=1
    tiletype=0
    timer=0
    font=load_font('ConsolaMalgun.ttf',14)
    bigfont=load_font('ConsolaMalgun.ttf',30)
    stat=Stat()
    pausenum=0
    mouse_x,mouse_y =0,0
    tile=Tile()
    current_time = get_time()




def exit():
    pass


def pause():
    global dice_num
    global chracter


def resume():
    global dice_num
    global chracter

def update():
    global map
    global move
    global chracter
    global tile
    global turntype
    global statbar





def draw():
    global dice_num
    global chracter
    global tile
    global statbar
    global statpng
    global timer
    global map
    global bigfont
    global turntype
    global actionnumber


    clear_canvas()
    handle_events()
    backpicture.draw_to_origin(0,0)
    stat.draw()
    drawcard(actionnumber)
    if turntype==10 or turntype ==9:
         bigfont.draw(200,100,"PRESS SPACE!",color=(230,0,0))
    if map.chracter.hp==0:
        game_framework.push_state(gameover)
    delay(0.01)


    update_canvas()

__author__ = 'kkk'
