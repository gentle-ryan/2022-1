

def effect(nominal_rate, npery):
    effect = (1 + nominal_rate/npery)**npery - 1
    return effect
