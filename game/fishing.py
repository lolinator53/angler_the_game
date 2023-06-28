import time
import random
import winsound

from game import chances
from game import master

import keyboard

pathResources = './resources/'


def fish():
    time.sleep(random.randrange(20))
    winsound.PlaySound(pathResources + 'bobber.wav', winsound.SND_FILENAME)
    print('Now!')
    t_start = time.time()
    keyboard.wait('space')
    t_diff = time.time() - t_start
    master.reward(chances.calc_chance(t_diff))
