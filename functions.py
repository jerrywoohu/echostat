from PIL import Image, ImageOps, ImageGrab
import pytesseract
import difflib
from CONSTANTS import *
from USER_CONFIG import *
import win32gui
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def screenshot_ow_window():
    toplist, winlist = [], []
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)

    game_window = [(hwnd, title) for hwnd, title in winlist if 'Overwatch' ==  title][0][0]

    win32gui.SetForegroundWindow(game_window)
    bbox = win32gui.GetWindowRect(game_window)
    time.sleep(0.1)
    screenshot = ImageGrab.grab(bbox)
    width, height = screenshot.size
    if height == 1440 or height == 1080 or height == 2160:
        return screenshot
    else:
        return crop_windows_decoration(screenshot)

def pad_image(image):
    right = 64
    left = 64
    top = 64
    bottom = 64
    width, height = image.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(image.mode, (new_width, new_height), (255, 255, 255))
    result.paste(image, (left, top))
    return result

def crop_windows_decoration(image):
    width, height = image.size
    return image.crop((8, 0, width-8, height-8))

def crop_ratio(image, ratio):
    width, height = image.size
    if width / height != ratio:
        if abs(width / height - ratio) <= .1:
            title_bar_height = height - (width / ratio)
            # print(str(title_bar_height))
            return image.crop((0, title_bar_height, width, height))
        else:
            new_width = height * SCREEN_RATIO
            diff = width - new_width
            return image.crop((diff / 2, 0, (diff/2) + new_width, height))
    else:
        return image

def get_image_by_region(source, region):
    left, top, right, bottom = region
    source_width, source_height = source.size
    scrap = source.crop((left * source_width, top * source_height, right * source_width, bottom * source_height))
    return scrap

def prep_image_for_ocr(image, point, mono, scale_brightness, channel):
    scrap = image
    scrap = scrap.convert('RGB')
    match channel.lower():
        case 'r':
            data = scrap.getdata()
            scrap.putdata([(d[0], d[0], d[0]) for d in data])

        case 'g':
            data = scrap.getdata()
            scrap.putdata([(d[1], d[1], d[1]) for d in data])

        case 'b':
            data = scrap.getdata()
            scrap.putdata([(d[2], d[2], d[2]) for d in data])

        case _:
            pass
    scrap = scrap.convert('L')
    if mono:
        scrap = scrap.point(lambda p: 255 if p > point else 0)
    else:
        if scale_brightness:
            histogram = scrap.histogram()
            max = point
            for index in range(len(histogram) - point): 
                if histogram[index + point] != 0:
                    max = index + point
            scrap = scrap.point(lambda p: __scale(p, point, max))
        else: 
            scrap = scrap.point(lambda p: p if p > point else 0)
    scrap = ImageOps.invert(scrap.convert('RGB'))
    scrap = pad_image(scrap)
    return scrap

def __scale(p, min, max):
    if p < min: return 0
    value = (p / max) * 255
    return 255 if value > 255 else value

def get_prepped_region(source, region, point=86, mono=False, scale_brightness=False, channel='all'):
    return prep_image_for_ocr(get_image_by_region(source, region), point, mono, scale_brightness, channel)

def ocr_on_stat(image):
    result = pytesseract.image_to_string(image, config=TESSERACT_CONFIG + ' -c tessedit_char_whitelist=0123456789:%')
    result = result.strip()
    if len(result) == 0:
        result = '0'
        pass
    result = result.replace('%', '')
    return result

def ocr_on_time(image):
    result = pytesseract.image_to_string(image, config=TESSERACT_CONFIG + ' -c tessedit_char_whitelist=0123456789:')
    result = result.strip()
    return_val = ['0', '0']
    # print(result)
    if ':' not in result:
        if len(result) >= 3:
            return_val = [result[:-2], result[-2:]]
        elif len(result) == 0:
            return_val = ['0', '0']
        else:
            return_val = ['0', result]
    else:
        return_val = result.split(':')
    return return_val

def ocr_on_hero(image):
    # weird font
    result = pytesseract.image_to_string(image, config=TESSERACT_CONFIG)
    result = result.strip()
    return result

def ocr_on_words(image):
    # very normal font
    result = pytesseract.image_to_string(image, config=TESSERACT_CONFIG)
    result = result.strip()
    return result

# def ocr_on_map(image):
#     result = pytesseract.image_to_string(image, config=TESSERACT_CONFIG)
#     result = result.strip()
#     if result.upper() == 'O':
#         result = '0'0
#     return result

def combine_stats(image):
    hero_name = get_prepped_region(image, STAT_REGIONS['hero_name_region'])
    # hero_name.show()
    match_time = get_prepped_region(image, STAT_REGIONS['match_time_region'], point=32, scale_brightness=True)
    # match_time.show()

    gstat1 = get_prepped_region(image, STAT_REGIONS['g_region1'])
    gstat2 = get_prepped_region(image, STAT_REGIONS['g_region2'])
    gstat3 = get_prepped_region(image, STAT_REGIONS['g_region3'])
    gstat4 = get_prepped_region(image, STAT_REGIONS['g_region4'])
    gstat5 = get_prepped_region(image, STAT_REGIONS['g_region5'])
    gstat6 = get_prepped_region(image, STAT_REGIONS['g_region6'])
    # gstat4.show()
    # gstat6.show()
    hstat1 = get_prepped_region(image, STAT_REGIONS['h_region1'])
    hstat2 = get_prepped_region(image, STAT_REGIONS['h_region2'])
    hstat3 = get_prepped_region(image, STAT_REGIONS['h_region3'])
    hstat4 = get_prepped_region(image, STAT_REGIONS['h_region4'])
    hstat5 = get_prepped_region(image, STAT_REGIONS['h_region5'])
    hstat6 = get_prepped_region(image, STAT_REGIONS['h_region6'])
    # hstat4.show()
    # hstat5.show()
    # hstat6.show()

    hstat1_name = get_prepped_region(image, STAT_REGIONS['h_region1_name'], scale_brightness=True)
    hstat2_name = get_prepped_region(image, STAT_REGIONS['h_region2_name'], scale_brightness=True)
    hstat3_name = get_prepped_region(image, STAT_REGIONS['h_region3_name'], scale_brightness=True)
    hstat4_name = get_prepped_region(image, STAT_REGIONS['h_region4_name'], scale_brightness=True)
    hstat5_name = get_prepped_region(image, STAT_REGIONS['h_region5_name'], scale_brightness=True)
    hstat6_name = get_prepped_region(image, STAT_REGIONS['h_region6_name'], scale_brightness=True)

    # hstat1_name.show()
    # hstat2_name.show()
    # hstat3_name.show()
    # hstat4_name.show()
    # hstat5_name.show()
    # hstat6_name.show()

    g_stats = {
        'eliminations': ocr_on_stat(gstat1),
        'objective_kills': ocr_on_stat(gstat2),
        'objective_time': ocr_on_time(gstat3),
        'hero_damage_done': ocr_on_stat(gstat4),
        'healing_done': ocr_on_stat(gstat5),
        'deaths': ocr_on_stat(gstat6)
    }

    h_stats = []
    h_stats.append({
        'value': ocr_on_stat(hstat1),
        'name': ocr_on_words(hstat1_name)
    })
    h_stats.append({
        'value': ocr_on_stat(hstat2),
        'name': ocr_on_words(hstat2_name)
    })
    h_stats.append({
        'value': ocr_on_stat(hstat3),
        'name': ocr_on_words(hstat3_name)
    })
    h_stats.append({
        'value': ocr_on_stat(hstat4),
        'name': ocr_on_words(hstat4_name)
    })
    h_stats.append({
        'value': ocr_on_stat(hstat5),
        'name': ocr_on_words(hstat5_name)
    })
    h_stats.append({
        'value': ocr_on_stat(hstat6),
        'name': ocr_on_words(hstat6_name)
    })

    match_result = {
        'hero_name': ocr_on_hero(hero_name),
        'match_time': ocr_on_time(match_time),
        # 'map_name': ocr_on_map(map_name),
        'general_stats': g_stats,
        'hero_stats': h_stats
    }

    return match_result

def get_joined_stats(stats, column_map, stat_map = None):
    return_value = []
    general_stats = stats['general_stats']
    hero_stats = match_hero_stats(stats['hero_stats'], stat_map)

    return_value.append(stats['match_time'][0])
    return_value.append(stats['match_time'][1])

    for key in column_map:
        if key == None:
            return_value.append('')
        else:
            stat = general_stats.get(key)
            if stat == None and stat_map != None: 
                stat = hero_stats.get(key)
            if stat != None: 
                return_value.append(stat)
    sep = '\t'
    return sep.join(return_value)

def get_pastable(match_result, hero=''):
    if hero == '':
        paste_into_sheets = get_joined_stats(match_result, COLUMN_MAP['general'])
    else:
        hero = hero.lower()
        try: 
            paste_into_sheets = get_joined_stats(match_result, COLUMN_MAP[hero], STAT_MAPS[hero])
        except:
            paste_into_sheets = get_joined_stats(match_result, COLUMN_MAP['general'])
            
    return paste_into_sheets

def match_hero_stats(hero_stats, stat_map):
    return_dictionary = {}
    for index, stat in enumerate(hero_stats):
        if stat_map and stat_map[index] != None:
            return_dictionary[stat_map[index]] = stat['value']
    return return_dictionary

def infer_hero(hero_stats):
    results = []
    for hero_name in STAT_MAPS:
        # stat_dict = filter(lambda x: x != None, STAT_MAPS[hero_name])
        stat_dict = []
        for stat_name in STAT_MAPS[hero_name]:
            if stat_name != None:
                stat_dict.append(stat_name.replace('_', ' '))
        # print(hero_name)
        count = 0
        for hero_stat in hero_stats:
            massaged_name = ' '.join(hero_stat['name'].replace('-', ' ').lower().split())
            # print(massaged_name)
            if massaged_name in stat_dict:
                count += 1
            else:
                matches = difflib.get_close_matches(massaged_name, stat_dict, n=1)
                # print(matches)
                count += len(matches)
        # print('\t', count)
        results.append({'hero_name': hero_name, 'value': count})
    highest = max(results, key=lambda x: x['value'])['value']
    return_value = []
    for result in results:
        if result['value'] == highest:
            return_value.append(result)
    return return_value