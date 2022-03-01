"""
Переписываем с использованием def
"""

import time

from wrap import world, sprite, sprite_text, actions


def voice(text,kto):
    #Приведение
    text = sprite.add_text(text, sprite.get_x(kto), sprite.get_top(kto) - 20, text_color=(228, 19, 15))
    time.sleep(0.5)
    sprite.remove(text)

def run(angle, rasstoinei):
    # побег
    actions.set_size_percent(victim, 30, 30, 500)
    actions.set_angle(victim, angle, 500)
    actions.move_at_angle_dir(victim, rasstoinei, 600)
    actions.set_size_percent(victim, 100, 100, 500)

def rost(upw,uph):
    actions.set_size_percent(godzila,upw,uph,200)

def run_after_hunter(rasstoinei,dvishenie_x,dvishenie_y):
    #погоня №2
    sprite.set_reverse_x(godzila,True)
    time.sleep(0.5)
    actions.move_at_angle_point(godzila,sprite.get_x(hunter)+dvishenie_x,sprite.get_y(hunter)+dvishenie_y,rasstoinei)

def run_after_him(rasstoinei):
    # погоня
    actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), rasstoinei, 500)

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

victim = sprite.add("pacman", 330, 100, "player2")
hunter = sprite.add("pacman", 150, 100, "enemy_blue_right1")
godzila = sprite.add("mario-enemies", sprite.get_x(hunter)-50 , sprite.get_y(hunter)+70, "armadillo_go")

voice("Убегаем",victim)

voice("Вот ты и попался",godzila)

rost(140,150)

run(190, 30)

run_after_hunter(100,-70,10)

rost(230,250)

voice("В погоню!",hunter)

run_after_him(100)

run_after_hunter(100,+80,0)

voice("Мы почти догнали!",hunter)

run_after_him(30)

voice("Чёрт, нас почти догнали!",victim)

run(130, 120)

