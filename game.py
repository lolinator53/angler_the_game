import os
import _pickle as pickle
from classes import Player
from game import fishing
from ui import menu


if __name__ == '__main__':
    if os.path.exists('./resources/player.pkl'):
        with open('./resources/player.pkl', 'wb') as p:
            player = pickle.load(p)
    else:
        player = Player([], 0)
    sel = menu.start_menu(player, ['Go fishing', 'Inventory', 'Marketplace', 'Controls', 'Finish'], 'cyan')
    if sel == 0:
        fishing.fish()
    if sel == 3:
        menu.controls_menu()
        fishing.fish()
    if sel == 4:
        exit(0)
