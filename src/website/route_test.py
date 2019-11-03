from flask import render_template, Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def start():
    username = {"user":"NameDot"}
    return render_template("mirrur.html", title='Mirrur',time=datetime.year, \
           user=username)


if __name__ == '__main__':
    app.run()
