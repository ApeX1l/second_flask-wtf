import json
import random

from flask import Flask, render_template, redirect, request
from login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECretKeYApEx04'
sp = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию', 'климатолог',
      'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
      'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
count = 0


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


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    dictt = {
        'title': 'Anketa',
        'surname': 'Ivanov',
        'name': 'Oleg',
        'education': 'Vishee',
        'profession': 'Builder',
        'sex': 'Male',
        'motivation': 'Rabota',
        'ready': 'True'
    }
    return render_template('auto_answer.html', dictt=dictt)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        f = form.username_astronaut.data
        return redirect(f'/success/{f}')
    return render_template('login.html', title='Авторизация', form=form)


@app.route(f'/success/<username>')
def success(username):
    return render_template('success.html', username=username)


@app.route('/distribution')
def distribution():
    sp = ['Олег', 'Андрей', 'Ридли Скотт']
    return render_template('distribution.html', list=sp)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=age)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    global count
    if request.method == 'GET':
        with open('pictures_for_carousel', 'r') as f:
            al = list(map(lambda x: x.rstrip('\n'), f.readlines()))
            print(al)
        return render_template('galery.html', list=al)
    elif request.method == 'POST':
        count += 1
        f = request.files['file']
        with open(f'static/img/photo{count}.jpg', 'wb') as file:
            file.write(f.read())
        with open('pictures_for_carousel', 'a') as file:
            file.write(f'\nphoto{count}.jpg')
        return redirect('/galery')


@app.route('/member')
def member():
    with open("templates/peoples.json", "rt", encoding="utf8") as f:
        peoples_list = json.loads(f.read())
    ind = random.randrange(3)
    return render_template('member.html', peoples=peoples_list, index=ind)


if __name__ == '__main__':
    app.run()
