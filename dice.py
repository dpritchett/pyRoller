from random import randint

faces = {
    1: """ -----
|     |
|  o  |
|     |
 -----""",

    2: """ -----
| o   |
|     |
|   o |
 -----""",

    3: """ -----
| o   |
|  o  |
|   o |
 -----""",

    4: """ -----
| o o |
|     |
| o o |
 -----""",

    5: """ -----
| o o |
|  o  |
| o o |
 -----""",

    6: """ -----
| o o |
| o o |
| o o |
 -----"""
}


def roll(n=None):
    n = n or randint(1, 6)
    return faces[n]
