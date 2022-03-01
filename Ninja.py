import time, wrap
from wrap import world, sprite, sprite_text

world.set_back_color(0, 0, 130)
world.create_world(1000, 700, 250, 40)

cherepachka = sprite.add("mario-enemies", 50, 40, "turtle_stand")
sprite.set_height_proportionally(cherepachka, 70)
sprite.set_reverse_x(cherepachka, True)

cherepachka1 = sprite.add("mario-enemies", 50, 660, "turtle_stand")
sprite.set_height_proportionally(cherepachka1, 70)
sprite.set_reverse_x(cherepachka1, True)

cherepachka2 = sprite.add("mario-enemies", 960, 40, "turtle_stand")
sprite.set_height_proportionally(cherepachka2, 70)

cherepachka3 = sprite.add("mario-enemies", 960, 660, "turtle_stand")
sprite.set_height_proportionally(cherepachka3, 70)

privedenie = sprite.add("pacman", 950, 400, "enemy_red_left2", False)
sprite.set_height_proportionally(privedenie, 60)
while 1 == 1:
    sprite.move(cherepachka, 6, 0)
    sprite.move(cherepachka1, 0, -4)
    sprite.move(cherepachka2, 0, 4)
    sprite.move(cherepachka3,-6,0)