import time
import random
from game import chances
from game import master

import keyboard


def fish():
    time.sleep(random.randrange(20))
    print('Now!')
    t_start = time.time()
    keyboard.wait('space')
    t_diff = time.time() - t_start
    if t_diff != 0:
        print('time:', t_diff)
        master.reward(chances.calc_chance(t_diff))
