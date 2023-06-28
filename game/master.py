from ui.menu import menu
from game import fishing


def reward(result):
    if result > 9500:
        print('WOW!!! Legendary')
        decide(menu('WOW, you caught a legendary fish!', ['Fish again', 'Sell', 'Marketplace', 'Quit'], 'red'))
    elif result > 7000:
        print('gibe da purplez')
        decide(menu('That\'s a purple', ['Fish again', 'Sell', 'Marketplace', 'Quit'], 'red'))
    elif result > 3500:
        print('Blueberries ')
        decide(menu('Damn, blue', ['Fish again', 'Sell', 'Marketplace', 'Quit'], 'red'))
    elif result > 0:
        print('Could have been better (green)')
        decide(menu('I mean, better than nothing?', ['Fish again', 'Sell', 'Marketplace', 'Quit'], 'red'))
    else:
        print('go shower dude')
        decide(menu('Yeah, that\'s nothing', ['Fish again', 'Sell', 'Marketplace', 'Quit'], 'red'))


def decide(val):
    if val == 0:
        fishing.fish()
    elif val == 3:
        exit(0)