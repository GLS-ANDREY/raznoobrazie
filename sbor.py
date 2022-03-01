import random

import wrap

wrap.world.set_back_color(46, 115, 228)

wrap.world.create_world(1000, 700)

x = random.randint(1, 650)

t = random.randint(1, 900)

f = wrap.sprite.add("pacman", t, x, "player2")

wrap.sprite.set_size(f, 100, 100)

w = random.randint(1, 700)
d = random.randint(1, 600)

p = wrap.sprite.add("pacman", w, d, "item_apple")
p = wrap.sprite.add_text("point 1;)", w, d - 20)

e = random.randint(1, 700)
r = random.randint(1, 600)

u = wrap.sprite.add("pacman", e, r, "item_strawberry")
u = wrap.sprite.add_text("point 2=)", e, r - 20)

m = wrap.sprite.add("pacman", random.randint(1, 700), random.randint(1, 600), "item_cherry")
i = wrap.sprite.add_text("point 3^_^", wrap.sprite.get_x(m), wrap.sprite.get_y(m) - 20)

wrap.actions.move_to(f,t,d,2000)

wrap.actions.move_to(f,w,d,2000)

wrap.actions.move_to(f,w,r,2000)

wrap.actions.move_to(f,e,r,2000)

wrap.actions.move_to(f,e,wrap.sprite.get_y(m))

wrap.actions.move_to(f,wrap.sprite.get_x(m),wrap.sprite.get_y(m))
#wrap.actions.move_to(f,e,r,2000)

#wrap.actions.move_to(f,wrap.sprite.get_x(m),wrap.sprite.get_y(m))