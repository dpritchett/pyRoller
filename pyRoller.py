from flask import Flask
from random import choice

application = Flask(__name__)

dice_map = {
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

@application.route("/")
def hello():
    face = choice(dice_map)
    return "<pre>" + face + "</pre"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
