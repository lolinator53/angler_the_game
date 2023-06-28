import _pickle as pickle

from ui.menu import caught_menu
from game import fishing
from game import chances


def reward(result, fish):
    if result > 9500:
        fish.rarity = 'legendary'
        fish.name = chances.decide_name(fish.rarity)
        fish.weight = chances.calc_weight('legen')
        decide(caught_menu('legen.txt', fish))
    elif result > 8000:
        fish.rarity = 'purple'
        fish.name = chances.decide_name(fish.rarity)
        fish.weight = chances.calc_weight('purp')
        decide(caught_menu('purp.txt', fish))
    elif result > 5500:
        fish.rarity = 'blue'
        fish.name = chances.decide_name(fish.rarity)
        fish.weight = chances.calc_weight('blue')
        decide(caught_menu('blue.txt', fish))
    elif result > 0:
        fish.rarity = 'green'
        fish.name = chances.decide_name(fish.rarity)
        fish.weight = chances.calc_weight('green')
        decide(caught_menu('green.txt', fish))
    else:
        decide(caught_menu('nothing.txt', None))


def decide(val):
    if val[0] == 0:
        worth = eval_worth(val[1])
        fishing.fish()
    elif val[0] == 3:
        exit(0)

# TODO Wert mittels seltenheit und gewicht ermitteln
def eval_worth(weight):
    pass
