from functions import *
import ctypes
from ctypes import windll, wintypes
import os
import win32con

HOTKEY = (win32con.VK_F3, win32con.MOD_WIN)

def DoTheThing():
    screenshot = screenshot_ow_window()

    cropped = crop_ratio(screenshot, SCREEN_RATIO)
    cropped.show()
    match_result = combine_stats(cropped)
    print(match_result)

    inferred_hero = infer_hero(match_result['hero_stats'])

    if len(inferred_hero) == 0:
        print('error: could not infer hero')
        input_hero = ''
    elif len(STAT_MAPS) == len(inferred_hero):
        print('error: could not infer hero')
        return
    elif len(inferred_hero) == 1:
        print('inferred hero: ' + inferred_hero[0]['hero_name'])
        input_hero = inferred_hero[0]['hero_name']
    else:
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

vk, modifiers = HOTKEY
print("Registering key", vk)
if not ctypes.windll.user32.RegisterHotKey(None, 0, modifiers, vk):
    print("Unable to register id", 0)
try:
    msg = wintypes.MSG()
    while ctypes.windll.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            DoTheThing()
        ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
        ctypes.windll.user32.DispatchMessageA(ctypes.byref(msg))
finally:
    ctypes.windll.user32.UnregisterHotKey(None, 0)
