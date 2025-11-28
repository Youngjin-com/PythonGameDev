DATA = [
    [9,9,9,9,9],
    [9,0,0,0,9],
    [9,0,9,0,9],
    [9,0,0,0,9],
    [9,9,9,9,9],
]

def get_param():
    return len(DATA), len(DATA[0]), 80, "#ffa0ff", "#ffc080"

def init_player():
    return 120, 120, 45
