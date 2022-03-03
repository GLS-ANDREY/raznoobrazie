import time

import wrap
from wrap import world, sprite, sprite_text, actions

wrap.add_sprite_dir("my_sprite")
world.create_world(1200, 650)
fon_sprite = sprite.add("fon", 700, 325)
sprite.set_width_proportionally(fon_sprite, 1400)

# Cоздаем пакмена
pacman = sprite.add("pacman", 200, 300, "player2")
sprite.set_size(pacman, 50, 50)

# Создаем привидение
fantom = sprite.add("privedenie", 600, 325, "enemy_ill_blue1")
sprite.set_size(fantom, 40, 40)


@wrap.on_key_always(wrap.K_RIGHT, delay=15)
def povorot_right():
    get_pacman = sprite.get_angle(pacman)
    sprite.set_angle(pacman, get_pacman + 10)


@wrap.on_key_always(wrap.K_LEFT, delay=15)
def povorot_left():
    get_pacman = sprite.get_angle(pacman)
    sprite.set_angle(pacman, get_pacman - 10)


def top_stop():
    top_fantom = sprite.get_top(fantom)
    if top_fantom < 0:
        sprite.move_to(fantom, sprite.get_x(fantom), 20)


def bottom_stop():
    bottom_fantom = sprite.get_bottom(fantom)
    if bottom_fantom > 650:
        sprite.move_bottom_to(fantom, 650)


def left_stop():
    left_fantom = sprite.get_left(fantom)
    if left_fantom < 0:
        sprite.move_left_to(fantom, 0)


def right_stop():
    right_fantom = sprite.get_right(fantom)
    if right_fantom > 1200:
        sprite.move_right_to(fantom, 1200)


@wrap.always(10)
def move_prizrak(pos_x, pos_y):
    sprite.move_at_angle_point(fantom, pos_x, pos_y, 4)
    top_stop()
    bottom_stop()
    left_stop()
    right_stop()


@wrap.always(50)
def move_pacman():
    if sprite.get_costume(fantom) == "enemy_ill_blue1":
        sprite.move_at_angle_dir(pacman, 12)
        sprite.set_angle_to_point(pacman, sprite.get_x(fantom), sprite.get_y(fantom))


@wrap.on_key_down(wrap.K_t)
def invisible_true():
    sprite.set_costume(fantom,"enemy_inv")



@wrap.always
def proverka_invisible():
    if sprite.get_costume(fantom) == "enemy_inv":
        print("Сама скрытность")
