import curses
import os


def start_menu(player, classes, color='white'):
    def character(stdscr, ):
        attributes = {}
        icol = {
            1: 'blue',
            2: 'green',
            3: 'cyan',
            4: 'red',
            5: 'magenta',
            6: 'yellow',
            7: 'white'
        }
        col = {v: k for k, v in icol.items()}

        bc = curses.COLOR_BLACK

        curses.init_pair(1, 7, bc)
        attributes['normal'] = curses.color_pair(1)

        curses.init_pair(2, col[color], bc)
        attributes['highlighted'] = curses.color_pair(2)

        c = 0
        option = 0
        wallet = ''
        inv = ''
        if player.wallet <= 0 and not player.inventory:
            wallet = 'It seems your wallet and inventory are empty!\n'
        elif player.wallet <= 0:
            wallet = 'It seems your wallet is empty\n'
        elif not player.inventory:
            inv = 'It seems you are not holding any fish\n'
        else:
            wallet = 'Your wallet currently holds' + str(player.wallet) + 'fishlets.\n'
            inv = 'You currently have ' + str(len(player.inventory)) + 'fish in your inventory.\n'

        while c != 10:

            stdscr.erase()

            stdscr.addstr('Hey there and welcome to Angler.\n' + wallet + inv, curses.color_pair(1))

            refresh_cursor(classes, option, attributes, stdscr)
            c = stdscr.getch()

            option = check_input(c, option, classes)
        return option
    os.system('cls')
    return curses.wrapper(character)


def caught_menu(fish_file, fish):
    file = open('./resources/' + fish_file, 'r')
    color = file.readline()
    fish_art = file.read()

    def character(stdscr, ):
        attributes = {}
        options = ['Fish again', 'Sell', 'Visit Marketplace', 'Quit']
        bg_color = curses.COLOR_BLACK

        curses.init_pair(1, curses.COLOR_WHITE, bg_color)
        curses.init_pair(2, int(color), bg_color)
        curses.init_pair(3, 3, bg_color)

        attributes['normal'] = curses.color_pair(1)
        attributes['highlighted'] = curses.color_pair(3)

        char = 0
        option = 0
        while char != 10:
            stdscr.erase()
            stdscr.addstr('You caught a fish of the species \'' + str(fish.name) + '\' (Rarity: ' +
                          fish.rarity.capitalize() + ') with a weight of {:0.2f}kg.\n'.format(fish.weight),
                          curses.color_pair(1))
            stdscr.addstr(f'\n{fish_art}\n', curses.color_pair(2))
            stdscr.addstr('\n', curses.color_pair(1))

            refresh_cursor(options, option, attributes, stdscr)

            char = stdscr.getch()

            option = check_input(char, option, options)
        return [option, fish]
    os.system('cls')
    return curses.wrapper(character)


def controls_menu():
    def character(stdscr, ):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

        char = 0
        while char != 10:
            stdscr.erase()

            stdscr.addstr('To navigate the menus, use the arrow keys (e.g. Arrow Up and Arrow Down).\n',
                          curses.color_pair(1))
            stdscr.addstr('To select the highlighted menu option press the enter key.\n', curses.color_pair(1))
            stdscr.addstr('While fishing, press space bar when hearing the notification sound for your'
                          ' fishing bobber.\n', curses.color_pair(1))
            stdscr.addstr('> Start fishing\n', curses.color_pair(2))

            char = stdscr.getch()
        return
    os.system('cls')
    return curses.wrapper(character)


# #####################################################################################
# #                                    Util                                           #
# #####################################################################################


def refresh_cursor(classes, option, attributes, stdscr):
    for i in range(len(classes)):
        if i == option:
            attr = attributes['highlighted']
        else:
            attr = attributes['normal']

        stdscr.addstr(f'> ', attr)
        stdscr.addstr(f'{classes[i]}' + '\n', attr)


def check_input(char, option, options):
    if char == curses.KEY_UP and option == 0:
        option = len(options) - 1
    elif char == curses.KEY_UP and option > 0:
        option -= 1
    elif char == curses.KEY_DOWN and option < len(options) - 1:
        option += 1
    elif char == curses.KEY_DOWN and option == len(options) - 1:
        option = 0
    return option
