PREBREWERY = {1: 'Insert water',
              2: 'Waiting water',
              3: 'Stop water'}
BREWERY = {4: 'Initial boiling',
           5: 'Insert malt',
           6: 'Heating',
           7: 'Heat controll',
           8: 'Iodine test'}
FILTERING = {9: 'Open pot valve',
             10: 'Insert water',
             11: 'Check level',
             12: 'Stop water'}
BOILING = {13: 'Warm must',
           14: 'Add hop',
           15: 'Continue boiling'}
COOLING = {16: 'Turn on chiller',
           17: 'Check temperature'}
FERMENTATION = {18: 'Chill must',
                19: 'Maintain temperature',
                20: 'Process end'}


def get_stage(state):
    if state in PREBREWERY.values():
        return "Pre-brewery"
    elif state in BREWERY.values():
        return "Brewery"
    elif state in FILTERING.values():
        return "Filtering"
    elif state in BOILING.values():
        return "Boiling"
    elif state in COOLING.values():
        return "Cooling"
    elif state in FERMENTATION.values():
        return "Fermentation"


def get_state(state):
    if state in PREBREWERY.keys():
        return PREBREWERY.get(state)
    elif state in BREWERY.keys():
        return BREWERY.get(state)
    elif state in FILTERING.keys():
        return FILTERING.get(state)
    elif state in BOILING.keys():
        return BOILING.get(state)
    elif state in COOLING.keys():
        return COOLING.get(state)
    elif state in FERMENTATION.keys():
        return FERMENTATION.get(state)
