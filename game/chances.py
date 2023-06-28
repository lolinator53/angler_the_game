from random import randrange

randomrange = 9700  # 97.00

legen_names = ['Eagle ray', 'Minnow of the deep', 'Unicorn fish', 'Gigantic horse eater', 'Easter Bunny',
               'Threespine stickleback', "Azurewave Mystical Finale", "Coralcrest Celestial Harmony",
               "Marinersong Aquatic Echo", "Pearlshimmer Oceanic Symphony", "Sapphirestream Serene Serenade",
               "Seastarlight Enchanting Melody", "Rainbowglide Tranquil Sonata", "Tidalcrest Whispersong",
               "Opalwhisper Cascade Lullaby", "Moonstoneflow Aqua Rhapsody", "Neptunewave Harmonic Overture",
               "Lagoonbreeze Seraphic Cadence", "Coralglow Moonlit Crescendo", "Tritoncrest Ethereal Melody",
               "Aquavision Celestial Opus", "Marlincrest Oceanic Ballad", "Seashimmers Radiant Serenade",
               "Seashadowwave Azure Waltz", "Aquamist Melodic Serenade", "Coralwave Tranquil Sonnet",
               "Finwhispers Lustrous Mirage", "Seafinsplash Enchanted Echo", "Coralcascade Harmonious Whirl",
               "Seabreeze Harmonic Symphony", "Aqualush Radiant Rhapsody", "Marinersplash Oceanic Whispers",
               "Seastoneglide Serene Melody", "Opalcrest Seraphic Sonata", "Moonlitdancer Aquatic Serenade",
               "Seashimmer Harmony Mirage", "Tritonwhisper Ethereal Cadence"]

purple_names = ["Azurefin", "Marine Echo", "Coralwhisper", "Opal Serenade", "Moonstone Harmony", "Seashimmer",
                "Aquavista", "Lustrous Cascade", "Whisperwave", "Rainbow Rhapsody", "Tidalcrest", "Sapphire Lagoon",
                "Seastarlight", "Celestial Sonata", "Pearlglide", "Marinersplash", "Seabreeze Whirl",
                "Harmonic Serenade", "Coralcrest Mirage", "Seashadow Whisper"]

blue_names = ["Azurefin", "Marine Echo", "Coralwhisper", "Opal Harmony", "Moonstone Cascade", "Seashimmer", "Aquavista",
              "Lustrous Splash", "Whisperwave", "Rainbow Glint", "Tidalcrest", "Sapphire Lagoon", "Seastarlight",
              "Celestial Melody", "Pearlglide", "Marinersplash", "Seabreeze Whirl", "Harmonic Whisper",
              "Coralcrest Mirage", "Seashadow Whisper", "Aquamist", "Marlincrest", "Radiant Serenade", "Crystalwave",
              "Moonlit Splash", "Coralglow", "Enchanted Echo", "Opalcrest", "Aquatic Serenade", "Seashimmer Harmony",
              "Tritonwhisper"]

green_names = ["Azurefin", "Marine Echo", "Coralwhisper", "Opal", "Moonstone Cascade", "Seashimmer", "Aquavista",
               "Lustrous Splash", "Whisperwave", "Rainbow Glint", "Tidalcrest", "Sapphire Lagoon", "Seastarlight",
               "Celestial", "Pearlglide", "Marinersplash", "Seabreeze Whirl", "Whisper", "Coralcrest Mirage",
               "Seashadow", "Aquamist", "Marlincrest", "Radiant", "Crystalwave", "Moonlit Splash", "Coralglow",
               "Enchanted Echo", "Opalcrest", "Aquatic Chaos", "Seashimmer", "Tritonwhisper", "Silverscale",
               "Glimmer", "Marble", "Abyss", "Jewelfin", "Crimson", "Ember", "Goldenwave", "Aurorafin", "Silverstreak",
               "Sunkiss", "Iridescent", "Whitewave", "Cobalt", "Azureglow", "Turquoisewisp", "Amber", "Scarlet",
               "Velvetfin", "Oceanic"]


def calc_chance(timing):
    if timing < 0.5:
        result = randrange(randomrange) + 500
    elif timing < 2:
        result = randrange(randomrange)
    else:
        result = randrange(randomrange) - 10000
    return result


def calc_weight(rarity):
    dec = randrange(1, 99) / 100
    match rarity:
        case 'legen':
            weight = randrange(25, 50) + dec
        case 'purp':
            weight = randrange(15, 30) + dec
        case 'blue':
            weight = randrange(5, 20) + dec
        case 'green':
            weight = randrange(1, 6) + dec
        case _:
            weight = 0
    return weight


def decide_name(rarity):
    match rarity:
        case 'legendary':
            return legen_names[randrange(0, len(legen_names) - 1)]
        case 'purple':
            return purple_names[randrange(0, len(purple_names) - 1)]
        case 'blue':
            return blue_names[randrange(0, len(blue_names) - 1)]
        case _:
            return green_names[randrange(0, len(green_names) - 1)]
