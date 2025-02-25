import json

from flask import Flask, render_template, redirect
from login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECretKeYApEx04'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run()
