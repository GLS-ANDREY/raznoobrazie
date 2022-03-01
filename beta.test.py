import time
from wrap import world, sprite, sprite_text

posledniy_vistrel = time.time()
while 11 == 11:
    time.sleep(0.5)
    print(".")
    vreme = time.time() - posledniy_vistrel
    if vreme >= 3:
        print("Огонь")
        posledniy_vistrel = time.time()