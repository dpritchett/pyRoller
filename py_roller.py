from flask import Flask
from flask import abort

from dice import roll

application = Flask(__name__)


@application.route("/")
def root():
    return preformat()


@application.route("/<int:n>")
def show_face(n):
    if n < 1 or n > 6:
        abort(422)
    else:
        return preformat(n)


def preformat(n=None):
    face = roll(n)
    return "<pre>" + face + "</pre>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
