import time

import wrap
from wrap import world, sprite, sprite_text, actions

world.create_world(1200, 700)
world.set_back_color(17, 228, 0)

# Cоздаем пакмена
pacman = sprite.add("pacman", 200, 300, "player2")
sprite.set_size(pacman, 50, 50)

# Создаем привидение
fantom = sprite.add("pacman", 300, 300, "enemy_ill_blue1",False)
sprite.set_size(fantom, 110, 110)


@wrap.on_key_always(wrap.K_RIGHT, delay=15)
def povorot_right():
    get_pacman = sprite.get_angle(pacman)
    sprite.set_angle(pacman, get_pacman + 10)


@wrap.on_key_always(wrap.K_LEFT, delay=15)
def povorot_left():
    get_pacman = sprite.get_angle(pacman)
    sprite.set_angle(pacman, get_pacman - 10)


@wrap.on_mouse_move
def move_prizrak(pos_x,pos_y):
    sprite.move_to(fantom,pos_x,pos_y)

@wrap.always(50)
def move_pacman(pos_x,pos_y):
    if sprite.is_visible(fantom) == True:
        sprite.move_at_angle_dir(pacman,12)
        sprite.set_angle_to_point(pacman,sprite.get_x(fantom),sprite.get_y(fantom))


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def invisible_false():
    sprite.show(fantom)


@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def invisible_true():
    sprite.hide(fantom)


@wrap.always
def top_stop():
    fantom_y = sprite.get_y(fantom)
    print(fantom_y)
    if fantom_y < 22:
       print("вверх")
