TESSERACT_CONFIG = '--psm 7'

screen_ratio = 16/9

STAT_REGIONS = {
    'hero_name_region': (0.492187500, 0.763888889, 0.687500000, 0.809722222),

    'match_time_region': (0.052734375, 0.048611111, 0.091796875, 0.065277778),

    'g_region1': (0.066406250, 0.819444444, 0.144531250, 0.854166667),
    'g_region2': (0.195312500, 0.819444444, 0.273437500, 0.854166667),
    'g_region3': (0.326171875, 0.819444444, 0.404296875, 0.854166667),
    'g_region4': (0.066406250, 0.879166667, 0.144531250, 0.913888889),
    'g_region5': (0.195312500, 0.879166667, 0.273437500, 0.913888889),
    'g_region6': (0.326171875, 0.879166667, 0.404296875, 0.913888889),

    'h_region1': (0.535156250, 0.819444444, 0.613281250, 0.854166667),
    'h_region2': (0.675781250, 0.819444444, 0.753906250, 0.854166667),
    'h_region3': (0.816406250, 0.819444444, 0.894531250, 0.854166667),
    'h_region4': (0.535156250, 0.879166667, 0.613281250, 0.913888889),
    'h_region5': (0.675781250, 0.879166667, 0.753906250, 0.913888889),
    'h_region6': (0.816406250, 0.879166667, 0.894531250, 0.913888889),

    'h_region1_name': (0.535156250, 0.854166667, 0.675781250, 0.875000000),
    'h_region2_name': (0.675781250, 0.854166667, 0.816406250, 0.875000000),
    'h_region3_name': (0.816406250, 0.854166667, 0.957031250, 0.875000000),
    'h_region4_name': (0.535156250, 0.909722222, 0.675781250, 0.930555556),
    'h_region5_name': (0.675781250, 0.909722222, 0.816406250, 0.930555556),
    'h_region6_name': (0.816406250, 0.909722222, 0.957031250, 0.930555556),
}


STAT_MAPS = {
    'dva':              ['weapon_accuracy', 'kill_streak_best', 'damage_blocked', 'self_destruct_kills', 'mechs_called', None],
    'orisa':            ['weapon_accuracy', 'kill_streak_best', 'damage_blocked', 'offensive_assists', 'damage_amplified', None],
    'reinhardt':        ['damage_blocked', 'kill_streak_best', 'charge_kills', 'fire_strike_kills', 'earth_shatter_kills', None],
    'roadhog':          ['weapon_accuracy', 'kill_streak_best', 'enemies_hooked', 'hook_accuracy', 'self_healing', 'whole_hog_kills'],
    'sigma':            ['damage_blocked', 'kill_streak_best', 'damage_absorbed', 'accretion_kills', 'gravitic_flux_kills', None],
    'winston':          ['damage_blocked', 'kill_streak_best', 'melee_kills', 'players_knocked_back', 'primal_rage_kills', None],
    'wrecking_ball':    ['weapon_accuracy', 'kill_streak_best', 'final_blows', 'grappling_claw_kills', 'piledriver_kills', 'minefield_kills'],
    'zarya':            ['damage_blocked', 'kill_streak_best', 'high_energy_kills', 'average_energy', 'graviton_surge_kills', None],

    'ana':              ['unscoped_accuracy', 'scoped_accuracy', 'defensive_assists', 'nano_boost_assists', 'enemies_slept', None],
    'baptiste':         ['weapon_accuracy', 'healing_accuracy', 'damage_amplified', 'amplification_matrix_assists', 'defensive_assists', 'immortality_field_deaths_prevented'],
    'brigitte':         ['offensive_assists', 'defensive_assists', 'damage_blocked', 'armor_provided', 'inspire_uptime_percentage', None],
    'lucio':            ['weapon_accuracy', 'kill_streak_best', 'sound_barriers_provided', 'offensive_assists', 'defensive_assists', None],
    'mercy':            ['offensive_assists', 'defensive_assists', 'players_resurrected', 'blaster_kills', 'damage_amplified', None],
    'moira':            ['secondary_fire_accuracy', 'kill_streak_best', 'defensive_assists', 'coalescence_kills', 'coalescence_healing', 'self_healing', None],
    'zenyatta':         ['weapon_accuracy', 'kill_streak_best', 'offensive_assists', 'defensive_assists', 'transcendence_healing', None]
}

SHEET_MAPS = {
    'general':          ['eliminations', 'deaths', 'hero_damage_done', 'healing_done'],
    'reinhardt':        ['eliminations', 'deaths', 'hero_damage_done', 'damage_blocked'],
    'ana':              ['eliminations', 'deaths', 'hero_damage_done', 'healing_done', 'enemies_slept', 'unscoped_accuracy', 'scoped_accuracy'],
    'brigitte':         ['eliminations', 'deaths', 'hero_damage_done', 'healing_done', 'damage_blocked', 'inspire_uptime_percentage'],
    'moira':            ['eliminations', 'deaths', 'hero_damage_done', 'healing_done', 'coalescence_kills']
}