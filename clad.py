import wrap, random, math

wrap.world.set_back_color(0, 0, 130)

wrap.world.create_world(1000, 700, 250, 40)

p = 100
m = 200

cherepachka = wrap.sprite.add("mario-enemies", p, m, "turtle_stand")
wrap.sprite.set_height_proportionally(cherepachka, 80)
wrap.sprite.set_reverse_x(cherepachka, True)
dot = wrap.sprite.add("pacman", p, m, "dot")

t = random.randint(100, 700)

x = random.randint(200, 600)

clad = wrap.sprite.add("mario-enemies", t, x, "cloud", False)
a = math.dist([p, m], [t, x])
a = int(a)
a = str(a)
wrap.sprite.add_text("До клада " + a + "px", 150, 130)

wrap.actions.set_angle_to_point(cherepachka, t, x)

q = input("Куда идти по X:")
q = int(q)
o = input("Куда идти по Y:")
o = int(o)
wrap.actions.move_to(cherepachka, q, o)
p = wrap.sprite.get_x(cherepachka)
m = wrap.sprite.get_y(cherepachka)
a = math.dist([p, m], [t, x])
a = int(a)
a = str(a)
wrap.sprite.add_text("До клада " + a + "px", wrap.sprite.get_x(cherepachka), wrap.sprite.get_y(cherepachka) - 50)
wrap.sprite.add("pacman", p, m, "dot")
wrap.actions.set_angle_to_point(cherepachka,t,x)

n = input("Куда идти по X:")
n = int(n)
z = input("Куда идти по Y:")
z = int(z)
wrap.actions.move_to(cherepachka, n, z)
p = wrap.sprite.get_x(cherepachka)
m = wrap.sprite.get_y(cherepachka)
a = math.dist([p, m], [t, x])
a = int(a)
a = str(a)
wrap.sprite.add_text("До клада " + a + "px", wrap.sprite.get_x(cherepachka), wrap.sprite.get_y(cherepachka) - 50)
wrap.sprite.add("pacman", p, m, "dot")
wrap.actions.set_angle_to_point(cherepachka,t,x)

h = input("Куда идти по X:")
h = int(h)
j = input("Куда идти по Y:")
j = int(j)
wrap.actions.move_to(cherepachka, h, j)

wrap.sprite.add("pacman", wrap.sprite.get_x(cherepachka), wrap.sprite.get_y(cherepachka), "dot")

a = math.dist([wrap.sprite.get_x(cherepachka), wrap.sprite.get_y(cherepachka)], [t, x])
a = int(a)
a = str(a)
wrap.sprite.add_text("До клада " + a + "px", wrap.sprite.get_x(cherepachka), wrap.sprite.get_y(cherepachka) - 50)

wrap.actions.set_angle_to_point(cherepachka, t, x)

wrap.sprite.show(clad)