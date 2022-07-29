from PIL import Image, ImageGrab, ImageOps, PngImagePlugin, JpegImagePlugin, ImageEnhance
from ctypes import windll
import pytesseract
import time
import os
import difflib
from CONSTANTS import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# sample_image = './samples/sample0.jpg'
sample_image = ''

def pad_image(image):
    right = 48
    left = 48
    top = 48
    bottom = 48
    width, height = image.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(image.mode, (new_width, new_height), (0, 0, 0))
    result.paste(image, (left, top))
    return result

def crop_ratio(image, ratio):
    width, height = image.size
    if width / height != ratio:
        if abs(width / height - ratio) <= .1:
            title_bar_height = height - (width / ratio)
            # print(str(title_bar_height))
            return image.crop((0, title_bar_height, width, height))
        else:
            new_width = height * screen_ratio
            diff = width - new_width
            return image.crop((diff / 2, 0, (diff/2) + new_width, height))
    else:
        return image

def get_image_by_region(source, region, point=168, mono=False, contrast = 1):
    left, top, right, bottom = region
    source_width, source_height = source.size
    scrap = cropped.crop((left * source_width, top * source_height, right * source_width, bottom * source_height))
    scrap = pad_image(scrap)
    if contrast != 1:
        scrap = ImageEnhance.Contrast(scrap).enhance(contrast)
    # scrap = ImageOps.invert(scrap.convert('RGB'))
    scrap = scrap.convert('L')
    # scrap.show()
    if mono:
        scrap = scrap.point(lambda p: 255 if p > point else 0)
    else:
        scrap = scrap.point(lambda p: p if p > point else 0)
    # scrap = scrap.convert('1')
    # scrap.show()
    return scrap

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
    hero_name = get_image_by_region(image, STAT_REGIONS['hero_name_region'])
    # hero_name.show()
    match_time = get_image_by_region(image, STAT_REGIONS['match_time_region'], point=100, contrast=3.5)
    # match_time.show()

    gstat1 = get_image_by_region(image, STAT_REGIONS['g_region1'])
    gstat2 = get_image_by_region(image, STAT_REGIONS['g_region2'])
    gstat3 = get_image_by_region(image, STAT_REGIONS['g_region3'])
    gstat4 = get_image_by_region(image, STAT_REGIONS['g_region4'])
    gstat5 = get_image_by_region(image, STAT_REGIONS['g_region5'])
    gstat6 = get_image_by_region(image, STAT_REGIONS['g_region6'])

    hstat1 = get_image_by_region(image, STAT_REGIONS['h_region1'])
    hstat2 = get_image_by_region(image, STAT_REGIONS['h_region2'])
    hstat3 = get_image_by_region(image, STAT_REGIONS['h_region3'])
    hstat4 = get_image_by_region(image, STAT_REGIONS['h_region4'])
    hstat5 = get_image_by_region(image, STAT_REGIONS['h_region5'])
    hstat6 = get_image_by_region(image, STAT_REGIONS['h_region6'])
    # hstat4.show()
    # hstat5.show()
    # hstat6.show()

    hstat1_name = get_image_by_region(image, STAT_REGIONS['h_region1_name'], point=100, contrast=2.5)
    hstat2_name = get_image_by_region(image, STAT_REGIONS['h_region2_name'], point=100, contrast=2.5)
    hstat3_name = get_image_by_region(image, STAT_REGIONS['h_region3_name'], point=100, contrast=2.5)
    hstat4_name = get_image_by_region(image, STAT_REGIONS['h_region4_name'], point=100, contrast=2.5)
    hstat5_name = get_image_by_region(image, STAT_REGIONS['h_region5_name'], point=100, contrast=2.5)
    hstat6_name = get_image_by_region(image, STAT_REGIONS['h_region6_name'], point=100, contrast=2.5)

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

def get_joined_stats(stats, hero_map, stat_map = None):
    return_value = []
    general_stats = stats['general_stats']
    hero_stats = match_hero_stats(match_result['hero_stats'], stat_map)

    return_value.append(stats['match_time'][0])
    return_value.append(stats['match_time'][1])

    for key in hero_map:
        stat = general_stats.get(key)
        if stat == None and stat_map != None: 
            stat = hero_stats.get(key)
        if stat != None: 
            return_value.append(stat)
    sep = '\t'
    return sep.join(return_value)

def get_pastable(match_result, hero=''):
    if hero == '':
        paste_into_sheets = get_joined_stats(match_result, SHEET_MAPS['general'])
    else:
        hero = hero.lower()
        try: 
            paste_into_sheets = get_joined_stats(match_result, SHEET_MAPS[hero], STAT_MAPS[hero])
        except:
            paste_into_sheets = get_joined_stats(match_result, SHEET_MAPS['general'])
            
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

while True:

    # try:
    if sample_image == '':
        try:
            screenshot = ImageGrab.grabclipboard()
        except:
            pass
    else:
        screenshot = Image.open(sample_image)
    # print(type(screenshot))
    if isinstance(screenshot, PngImagePlugin.PngImageFile) or isinstance(screenshot, JpegImagePlugin.JpegImageFile):
        detected = True
        print('screenshot detected')
        cropped = crop_ratio(screenshot, screen_ratio)
        if sample_image == '':
            cropped.show()
        match_result = combine_stats(cropped)
        print(match_result)

        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()

        # paste_into_sheets = get_pastable(match_result)
        # command = 'echo ' + paste_into_sheets + '| clip'
        # os.system(command)

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

        
        paste_into_sheets = get_pastable(match_result, input_hero)
        command = 'echo ' + paste_into_sheets + '| clip'
        os.system(command)
        print('copied to clipboard')

    # except:
    #     print('clipboard invalid')
    time.sleep(3)