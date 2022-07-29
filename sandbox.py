from PIL import Image, ImageGrab, ImageOps
import time
import difflib
from CONSTANTS import *

hero_stats = [{'value': '0', 'name': 'UNSCOPED ACCURACY'}, {'value': '0', 'name': 'SCOPED ACCURACY'}, {'value': '0', 'name': 'DEFENSIVE ASSISTS'}, {'value': '0', 'name': 'NANO BOOST ASSISTS'}, {'value': '0', 'name': 'ENEMIES SLEPT'}, {'value': '0', 'name': 'ee'}]

results = []
for hero_name in STAT_MAPS:
    stat_dict = filter(lambda x: x != None, STAT_MAPS[hero_name])
    # print(hero_name)
    count = 0
    for hero_stat in hero_stats:
        massaged_name = hero_stat['name'].replace(' ', '_').lower()
        # print(massaged_name)
        if massaged_name in stat_dict:
            count += 1
        else:
            matches = difflib.get_close_matches(massaged_name, stat_dict, n=1)
            # print(matches)
            count += len(matches)
    # print('\t', count)
    results.append({'key': hero_name, 'value': count})
highest = max(results.values())
return results.filter(lambda x: x['value'] == highest)