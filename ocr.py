from PIL import ImageGrab, PngImagePlugin, JpegImagePlugin
from functions import *
from ctypes import windll
import time
import os

while True:

    try:
        screenshot = ImageGrab.grabclipboard()
    except:
        pass

    if isinstance(screenshot, PngImagePlugin.PngImageFile) or isinstance(screenshot, JpegImagePlugin.JpegImageFile):
        detected = True
        print('screenshot detected')
        cropped = crop_ratio(screenshot, SCREEN_RATIO)
        cropped.show()
        match_result = combine_stats(cropped)
        print(match_result)

        inferred_hero = infer_hero(match_result['hero_stats'])
        match len(inferred_hero):
            case 0:
                print('error: could not infer hero')
                input_hero = ''
            case 1:
                print('inferred hero: ' + inferred_hero[0]['hero_name'])
                input_hero = inferred_hero[0]['hero_name']
            case _:
                print('multiple heros inferred')
                for hero in inferred_hero: 
                    print(hero)
                input_hero = input('hero: ')

        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()

        paste_into_sheets = get_pastable(match_result, input_hero)
        command = 'echo ' + paste_into_sheets + '| clip'
        os.system(command)
        print('copied to clipboard')

    time.sleep(3)