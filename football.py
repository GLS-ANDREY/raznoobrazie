import time

from wrap import world, sprite, sprite_text, actions

world.create_world(400, 600, 900, 50)
world.set_back_color(17, 228, 0)

# Создаём игрков
player1 = sprite.add("mario-1-big", 300, 180, "stand")
sprite.set_reverse_x(player1, True)
player2 = sprite.add("mario-2-big", 130, 100, "stand")
player3 = sprite.add("mario-3-big", 100, 330, "stand")

# Создаем мяч
ball = sprite.add("mario-enemies", sprite.get_x(player3) + 30, sprite.get_y(player3) + 20)


def pas_igrok(komu):
    if sprite.get_angle(komu) == -90:
        actions.move_to(ball, sprite.get_x(komu) - 30, sprite.get_y(komu) + 20)
    if sprite.get_angle(komu) == 90:
        actions.move_to(ball,sprite.get_x(komu) + 30, sprite.get_y(komu) + 20)



pas_igrok(player1)

pas_igrok(player2)

pas_igrok(player1)

pas_igrok(player3)

pas_igrok(player1)

pas_igrok(player2)

pas_igrok(player3)
