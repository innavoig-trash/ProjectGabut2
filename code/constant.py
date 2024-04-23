'''
Constants for the game
'''

NUMTILES = 10
TILESIZE = 58

WIDTH = NUMTILES * TILESIZE
HEIGHT = 10 * TILESIZE

FRAME = 60
ASSETS = '../assets'
PRIMARY = '#323443'

# DATA = [
#     '            ',
#     '            ',
#     '            ',
#     '   xxxx    x',
#     '  xxx     xx',
#     'xx    xxx xx',
#     'xxx     xxxx',
#     '   xxx      ',
#     '   xxx      ',
#     'x       xxx ',
#     'xx    xxxx  ',
#     'xxxx        ',
#     '  xxx       ',
#     '   p    xx  ',
#     '      xxxx  ',
#     'xxxxxxxxxxxx',
# ]

LEVEL = [
    {
        'background': '../levels/background.csv',
        'ornament': '../levels/ornament.csv',
        'character': '../levels/character.csv',
        'wall': '../levels/wall.csv',
        'bomb': '../levels/bomb.csv',
    }
]
