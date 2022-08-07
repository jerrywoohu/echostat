# None inserts a blank column
GENERAL_COLUMN_MAP = ['eliminations', 'deaths', 'hero_damage_done', 'healing_done']
COLUMN_MAP = {
    'general':          GENERAL_COLUMN_MAP,

    'dva':              ['eliminations', 'deaths', 'hero_damage_done', 'damage_blocked', 'self_destruct_kills'],
    'orisa':            ['eliminations', 'deaths', 'hero_damage_done', 'damage_blocked', 'damage_amplified', 'weapon_accuracy'],
    'reinhardt':        ['eliminations', 'deaths', 'hero_damage_done', 'damage_blocked'],
    'roadhog':          GENERAL_COLUMN_MAP + ['enemies_hooked', 'hook_accuracy'],
    'sigma':            ['eliminations', 'deaths', 'hero_damage_done', 'damage_blocked', 'damage_absorbed'],
    'winston':          ['eliminations', 'deaths', 'hero_damage_done', 'damage_blocked', 'primal_rage_kills'],
    'wrecking_ball':    GENERAL_COLUMN_MAP + ['minefield_kills', 'weapon_accuracy'],
    'zarya':            ['eliminations', 'deaths', 'hero_damage_done', 'damage_blocked', 'high_energy_kills', 'average_energy'],

    'ashe':             GENERAL_COLUMN_MAP + ['dynamite_kills', 'scoped_accuracy'],
    'bastion':          GENERAL_COLUMN_MAP + ['sentry_kills', 'weapon_accuracy'],
    'cassidy':          GENERAL_COLUMN_MAP + ['fan_the_hammer_kills', 'weapon_accuracy'],
    'doomfist':         GENERAL_COLUMN_MAP + ['shields_created', 'weapon_accuracy'],
    'echo':             GENERAL_COLUMN_MAP + ['sticky_bomb_kills', 'weapon_accuracy'],
    'genji':            GENERAL_COLUMN_MAP + ['dragonblade_kills', 'weapon_accuracy'],
    'hanzo':            GENERAL_COLUMN_MAP + ['critical_hits', 'weapon_accuracy'],
    'junkrat':          GENERAL_COLUMN_MAP + ['enemies_trapped', 'weapon_accuracy'],
    'mei':              GENERAL_COLUMN_MAP + ['enemies_frozen'],
    'pharah':           GENERAL_COLUMN_MAP + ['rocket_direct_kills', 'weapon_accuracy'],
    'reaper':           GENERAL_COLUMN_MAP + ['death_blossom_kills', 'weapon_accuracy'],
    'soldier_76':       GENERAL_COLUMN_MAP + ['helix_rocket_kills', 'weapon_accuracy'],
    'sombra':           GENERAL_COLUMN_MAP + ['enemies_hacked', 'weapon_accuracy'],
    'symmetra':         GENERAL_COLUMN_MAP + ['sentry_turret_kills'],
    'torbjorn':         GENERAL_COLUMN_MAP + ['turret_kills', 'weapon_accuracy'],
    'tracer':           GENERAL_COLUMN_MAP + ['pulse_bomb_kills', 'weapon_accuracy'],
    'widowmaker':       GENERAL_COLUMN_MAP + ['scoped_critical_hits', 'scoped_accuracy'],
    
    'ana':              GENERAL_COLUMN_MAP + ['enemies_slept', 'unscoped_accuracy', 'scoped_accuracy'],
    'baptiste':         GENERAL_COLUMN_MAP + ['immortality_field_deaths_prevented', 'weapon_accuracy', 'healing_accuracy'],
    'brigitte':         GENERAL_COLUMN_MAP + ['damage_blocked', 'inspire_uptime_percentage'],
    'lucio':            GENERAL_COLUMN_MAP + ['sound_barriers_provided', 'weapon_accuracy'],
    'mercy':            GENERAL_COLUMN_MAP + ['damage_amplified', 'players_resurrected', 'blaster_kills'],
    'moira':            GENERAL_COLUMN_MAP + ['coalescence_kills', 'self_healing'],
    'zenyatta':         GENERAL_COLUMN_MAP + ['offensive_assists']
}