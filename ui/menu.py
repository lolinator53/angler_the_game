import curses


def menu(title, classes, color='white'):
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
        while c != 10:

            stdscr.erase()

            stdscr.addstr(f"{title}\n", curses.color_pair(1))

            for i in range(len(classes)):
                if i == option:
                    attr = attributes['highlighted']
                else:
                    attr = attributes['normal']

                stdscr.addstr(f'> ', attr)
                stdscr.addstr(f'{classes[i]}' + '\n', attr)
            c = stdscr.getch()

            if c == curses.KEY_UP and option == 0:
                option = len(classes) - 1
            elif c == curses.KEY_UP and option > 0:
                option -= 1
            elif c == curses.KEY_DOWN and option < len(classes) - 1:
                option += 1
            elif c == curses.KEY_DOWN and option == len(classes) - 1:
                option = 0
        return option
    return curses.wrapper(character)
