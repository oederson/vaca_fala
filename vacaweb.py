from flask import Flask

app = Flask(__name__)

from views import *


def start():
    app.run()


if __name__ == '__main__':
    app.run(debug=True)


