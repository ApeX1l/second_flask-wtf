import json

from flask import Flask, render_template, redirect
from login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECretKeYApEx04'
sp = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию', 'климатолог',
      'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
      'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', work=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', type=list, sp=sp)


if __name__ == '__main__':
    app.run()
