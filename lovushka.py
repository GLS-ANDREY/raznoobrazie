import wrap, random

wrap.world.set_back_color(0, 0, 130)

wrap.world.create_world(1000, 700)

x = random.randint(1, 650)

t = random.randint(1, 900)

f = wrap.sprite.add("pacman", t, x, "player2")

wrap.actions.set_size(f, 75, 75)

w = random.randint(1, 700)
d = random.randint(1, 600)

p = wrap.sprite.add("pacman", w, d, "dot")

wrap.actions.set_angle_to_point(f, w, d)

wrap.actions.move_to(f, w, d, 2000)

wrap.sprite.remove(p)

l = wrap.sprite.add("pacman", w + random.randint(-50, 50), d - 130, "enemy_red_down1")

wrap.sprite.set_size(l, 90, 90)

y = wrap.sprite.add_text("Ага попался!", wrap.sprite.get_x(l), d - 200)

wrap.actions.set_angle(f, 180, 700)

# wrap.actions.move_at_angle_dir(f,350,700)

v = wrap.sprite.add("pacman", w, d + 90, "item_cherry")

wrap.sprite.set_size(v, 30, 30)

wrap.actions.move_to(f, w, d + 90)

wrap.sprite.remove(v)

wrap.sprite.set_size(f, 120, 120)

wrap.actions.set_angle(f, 0, 700)

wrap.sprite.remove(y)

wrap.actions.move_to(f, wrap.sprite.get_x(l), wrap.sprite.get_y(l))

wrap.sprite.remove(l)
