import time, wrap
from wrap import world, sprite, sprite_text

world.set_back_color(0, 0, 130)
world.create_world(1000, 700, 250, 40)

x = 50
y = 40

cherepachka = sprite.add("mario-enemies", x, y, "turtle_stand")
sprite.set_height_proportionally(cherepachka, 70)
sprite.set_reverse_x(cherepachka, True)
speed_y = 6

speed2_y = -10
lava = sprite.add("mario-enemies", 950, 40, "lava_ball")
sprite.set_height_proportionally(lava, 60)
sprite.set_angle(lava, 270)

stars = sprite.add("mario-items", sprite.get_x(cherepachka) + 50, sprite.get_y(cherepachka), "star")
x_lava = sprite.get_x(lava)
y_lava = sprite.get_y(lava)

chasi = time.time()
text = time.time() - chasi
text = int(text)
text = str(text)
text2 = sprite.add_text(text, 350, 50)


posledniy_vistrel = time.time()
while 1 == 1:
    text = time.time() - chasi
    text = int(text)
    text = str(text)
    sprite_text.set_text(text2, text)

    sprite.move(cherepachka, 0, speed_y)
    cordi = sprite.get_y(0)
    if 670 <= cordi:
        speed_y = -6
    if 30 >= cordi:
        speed_y = 6
    sprite.move(lava, 0, speed2_y)
    cordi2 = sprite.get_y(lava)
    if 670 <= cordi2:
        sprite.set_angle(lava, 90)
        speed2_y = -6
    if 20 >= cordi2:
        sprite.set_angle(lava, 270)
        speed2_y = 6

    vreme = time.time() - posledniy_vistrel
    if vreme >= 5:
        stars = sprite.add("mario-items", sprite.get_x(cherepachka) + 50, sprite.get_y(cherepachka), "star")
        x_lava = sprite.get_x(lava)
        y_lava = sprite.get_y(lava)
        posledniy_vistrel = time.time()

    if stars != None:
        sprite.move_at_angle_point(stars, x_lava, y_lava, 30)

    ugol_star = sprite.get_angle(stars)
    sprite.set_angle(stars, ugol_star + 10)

    pobeda = sprite.is_collide_sprite(lava, stars)
    if pobeda == True:
        break

while 11 == 11:
    sprite.hide(lava)
    time.sleep(0.5)
    sprite.show(lava)
    time.sleep(0.5)