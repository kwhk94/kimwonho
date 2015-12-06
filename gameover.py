import game_framework
import map
from pico2d import *
import battlemap


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image = load_image('png\\gameover.png')


def exit():
    # global image
    # del(image)
    close_canvas()


def update():
    pass

def draw():
    global image
    clear_canvas()
    image.clip_draw(0,0,800,600,400,300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.quit()


def pause(): pass


def resume(): pass




__author__ = 'kkk'
