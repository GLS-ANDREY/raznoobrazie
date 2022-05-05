import time

import wrap
from wrap import world, sprite, sprite_text

wrap.add_sprite_dir("my_sprite")
world.create_world(1200, 650)
fon_sprite = sprite.add("fon", 700, 325, "fon_pacman2")
sprite.set_width_proportionally(fon_sprite, 1400)
vremi = time.time()
stop = False
sprite.add_text("T = invisible", 45, 10, font_size=17)

# Cоздаем пакмена
pacman = sprite.add("pacman", 100, 325, "player2")
sprite.set_size(pacman, 50, 50)

# Создаем привидение
fantom = sprite.add("privedenie", 1100, 325, "enemy_ill_blue1")
sprite.set_size(fantom, 40, 40)

# Создаем сердца
life_fantom1 = sprite.add("heart", 1170, 30)
life_fantom2 = sprite.add("heart", 1130, 30)
life_fantom3 = sprite.add("heart", 1090, 30,"void_heart")

# Делаем таймер
chasi = time.time()
text = time.time() - chasi
text = int(text)
text = str(text)
text2 = sprite.add_text(text, 1055, 30)

# Создаем глаза для скилла
glaza = sprite.add("privedenie", 570, 635, "enemy_inv")

# Создаем фон для скилла
fon_black_skill = sprite.add("fon", 570, 630, "skill_fon_fake",False)

# Создаем обводку
border_white_skill = sprite.add("fon", 570, 627, "white_square")

# Делаем таймер для cкилла
chasi_skill = time.time()
text2_skill = sprite.add_text(text, 570, 627, font_size=25, bold=True, text_color=[99, 26, 121],visible=False)


def top_stop():
    top_fantom = sprite.get_top(fantom)
    if top_fantom < 0:
        sprite.move_to(fantom, sprite.get_x(fantom), 20)


def bottom_stop():
    bottom_fantom = sprite.get_bottom(fantom)
    if bottom_fantom > 605:
        sprite.move_bottom_to(fantom, 605)


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
    global vremi
    costume_fantom = sprite.get_costume(fantom)
    if stop == False and costume_fantom == "enemy_ill_blue1":
        sprite.set_costume(fantom, "enemy_inv")  # <- Заходит в невидимость
        vremi = time.time()


@wrap.always
def proverka_invisible():
    global stop
    global chasi_skill
    if sprite.get_costume(fantom) == "enemy_inv":
        time_invisible = time.time() - vremi
        if time_invisible > 3.0:
            sprite.set_costume(fantom, "enemy_ill_blue1")  # <- Фантом выходит из невидимости
            vid_taymera_nedostupen()
            chasi_skill = time.time()
            stop = True


def vid_taymera_dostupen():
    sprite.hide(fon_black_skill)
    sprite.hide(text2_skill)
    sprite.show(glaza)


def vid_taymera_nedostupen():
    sprite.hide(glaza)
    sprite.show(fon_black_skill)
    sprite.show(text2_skill)



@wrap.always
def taimer():
    text = time.time() - chasi
    text = int(text)
    text = str(text)
    sprite_text.set_text(text2, text)


@wrap.always
def taimer_skill():
    global text_skill
    global stop
    text_skill = time.time() - chasi_skill
    if True == stop:
        ostaloci = 16 - text_skill
        ostaloci = int(ostaloci)
        ostaloci = str(ostaloci)
        sprite_text.set_text(text2_skill, ostaloci)
    if text_skill > 16:
        stop = False
        vid_taymera_dostupen()