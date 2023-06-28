from game import fishing
from ui.menu import menu


if __name__ == '__main__':
    sel = menu('Hi', ['Fish', 'Inventory', 'Marketplace', 'Finish'], 'cyan')
    if sel == 0:
        fishing.fish()
    if sel == 3:
        exit(0)
