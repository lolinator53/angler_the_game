import random

randomrange = 10000  # 100.00


def calc_chance(timing):
    if timing < 0.5:
        result = random.randrange(randomrange) + 500
        print('res un:', result - 500)
    elif timing < 2:
        result = random.randrange(randomrange)
        print('res un:', result)
    else:
        result = random.randrange(randomrange) - 10000
        print('res un:', result + 10000)
    return result
