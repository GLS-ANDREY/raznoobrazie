import wrap,time
wrap.world.set_back_color(46,115,228)
ninja=1

wrap.world.create_world(1000,700)

wrap.sprite.add("pacman",300,400,"player2")

wrap.sprite.set_size(0,250,250)

wrap.sprite.add("mario-enemies",700,400,"mushroom")

wrap.sprite.set_size(ninja,150,150)

wrap.sprite.add_text("привет ниндзя",300,230)

time.sleep(1)

wrap.sprite.add_text("даров пакмен",650,230)

time.sleep(1)

wrap.sprite.add_text("ты помнишь про свой долг?",300,150)

time.sleep(1)

wrap.sprite.add_text("про какой ещё долг про что ты говоришь?",650,150)

time.sleep(1)

wrap.sprite.add_text("а ну значит не помнишь ну на тебе!!!",300,100)

time.sleep(1)

wrap.sprite.set_angle(0,45)

wrap.actions.move(0,270,-200)

wrap.sprite.set_angle(0,145)

wrap.sprite.set_costume(0,"player1")

wrap.actions.move_to(0,700,400)

wrap.sprite.remove(1)

wrap.sprite.set_costume(0,"player3")

time.sleep(1)

wrap.sprite.set_costume(0,"player1")

time.sleep(1)

wrap.sprite.set_costume(0,"player2")