import time

from wrap import world, sprite, sprite_text, actions

world.create_world(400, 600, 900, 50)
world.set_back_color(111, 18, 0)


def poyavlenie(gde_x, gde_y, kostum):
    # Появление 1 танка
    effect = sprite.add("battle_city_items", gde_x, gde_y, "effect_appearance1")
    time.sleep(0.3)
    sprite.set_costume(effect, "effect_appearance2")
    time.sleep(0.3)
    sprite.set_costume(effect, "effect_appearance3")
    time.sleep(0.3)
    sprite.set_costume(effect, "effect_appearance4")
    time.sleep(0.3)
    sprite.remove(effect)
    time.sleep(0.3)
    tank1 = sprite.add("battle_city_tanks", gde_x, gde_y, kostum)
    return tank1


def move_right(tank, poexali_right):
    # Движение вправо
    actions.set_angle(tank, 90)
    actions.move(tank, poexali_right, 0)


def move_left(tank, poexali_left):
    # Движение влево
    actions.set_angle(tank, -90)
    actions.move(tank, -poexali_left, 0)


def move_up(tank, poexali_up):
    actions.set_angle(tank, 0)
    actions.move(tank, 0, -poexali_up)


def move_down(tank, poexali_down):
    actions.set_angle(tank, 180)
    actions.move(tank, 0, poexali_down)


def vistrel(tank_puli, polet):
    # Верх танк1
    if sprite.get_angle(tank_puli) == 0:
        bullet1 = sprite.add("battle_city_items", sprite.get_x(tank_puli), sprite.get_y(tank_puli) - 23, "bullet")
        actions.move(bullet1, 0, -polet, 1500)
        time.sleep(0.3)
        sprite.remove(bullet1)
    # Вниз танк2
    if sprite.get_angle(tank_puli) == 180:
        bullet1 = sprite.add("battle_city_items", sprite.get_x(tank_puli), sprite.get_y(tank_puli) + 23, "bullet")
        sprite.set_angle(bullet1, 180)
        actions.move(bullet1, 0, polet, 1650)
        time.sleep(0.4)
        sprite.remove(bullet1)
    # Вправо общее
    if sprite.get_angle(tank_puli) == 90:
        bullet1 = sprite.add("battle_city_items", sprite.get_x(tank_puli) + 23, sprite.get_y(tank_puli), "bullet")
        sprite.set_angle(bullet1, 90)
        actions.move(bullet1, polet, 0, 1650)
        time.sleep(0.3)
        sprite.remove(bullet1)
    # Влево общее
    if sprite.get_angle(tank_puli) == -90:
        bullet1 = sprite.add("battle_city_items", sprite.get_x(tank_puli) - 23, sprite.get_y(tank_puli), "bullet")
        sprite.set_angle(bullet1, -90)
        actions.move(bullet1, -polet, 0, 1650)
        time.sleep(0.3)
        sprite.remove(bullet1)


def vzriv():
    vzrivtank = sprite.add("battle_city_items", 100, 100, "effect_explosion1")
    time.sleep(0.6)
    sprite.hide(vzrivtank)
    time.sleep(0.5)
    sprite.show(vzrivtank)
    time.sleep(0.6)
    sprite.hide(vzrivtank)
    time.sleep(0.5)
    sprite.show(vzrivtank)
    time.sleep(0.6)
    sprite.hide(vzrivtank)
    time.sleep(0.5)
    sprite.show(vzrivtank)
    time.sleep(0.3)
    sprite.remove(vzrivtank)


def vzriv2(tank_effect):
    vzrivtank2 = sprite.add("battle_city_items", sprite.get_x(tank_effect) - 8, sprite.get_y(tank_effect)+3, "effect_explosion2")
    time.sleep(0.3)
    sprite.set_costume(vzrivtank2, "effect_explosion3")
    time.sleep(0.3)
    sprite.set_costume(vzrivtank2, "effect_explosion2")
    time.sleep(0.3)
    sprite.set_costume(vzrivtank2, "effect_explosion3")
    time.sleep(0.3)
    sprite.set_costume(vzrivtank2, "effect_explosion2")
    time.sleep(0.3)
    sprite.set_costume(vzrivtank2, "effect_explosion3")
    time.sleep(0.3)
    sprite.remove(vzrivtank2)


poyavlenie_tank1 = poyavlenie(150, 400, "tank_enemy_size1_green1")
sprite.set_angle(poyavlenie_tank1, 0)

poyavlenie_tank2 = poyavlenie(150, 100, "tank_enemy_size1_purple1")
sprite.set_angle(poyavlenie_tank2, 180)

move_right(poyavlenie_tank1, 60)

move_right(poyavlenie_tank2, 80)

move_up(poyavlenie_tank1, 0)

move_down(poyavlenie_tank2, 0)

vistrel(poyavlenie_tank2,290)

vistrel(poyavlenie_tank1,300)

move_left(poyavlenie_tank1, 60)

move_left(poyavlenie_tank2, 80)

move_up(poyavlenie_tank1, 0)

move_down(poyavlenie_tank2, 0)

finaltank = poyavlenie(200, 300, "tank_enemy_size4_green1")
sprite.set_angle(finaltank, 0)

vistrel(finaltank, 200)

move_right(finaltank, 0)

vistrel(finaltank, 150)

move_down(finaltank, 0)

vistrel(finaltank, 200)

move_left(finaltank, 0)

vistrel(finaltank, 150)

move_up(finaltank, 0)

sprite.remove(finaltank)

vistrel(poyavlenie_tank2, 170)

move_up(poyavlenie_tank1, 30)

vistrel(poyavlenie_tank1, 240)

vzriv2(poyavlenie_tank2)

time.sleep(0.4)

sprite.remove(poyavlenie_tank2)