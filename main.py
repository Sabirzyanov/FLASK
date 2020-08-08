from flask import Flask, render_template, request
from data import db_session
from data.hardware import Hardware

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'gayGard'
db_session.global_init('db/GDB.db')


@app.route('/')
def main():
    session = db_session.create_session()
    s = request.args.get('s')
    if s:
        hardwareList = session.query(Hardware).filter(Hardware.spec.contains(s))
        return render_template('index.html', hardwareList=hardwareList, pageTitle='Поиск')
    else:
        return render_template('index.html', pageTitle='Главная')


@app.route('/cpu/<string:type>/<string:socket>')
def cpu(type, socket):
    session = db_session.create_session()
    cpuList = session.query(Hardware).filter(Hardware.hardware_type == 'cpu', Hardware.name.contains(type),
                                             Hardware.spec.contains(socket))
    return render_template('index.html', hardwareList=cpuList, pageTitle='Процы ' + type)


@app.route('/motherboard/<string:socket>')
def motherboard(socket):
    session = db_session.create_session()
    motherboardList = session.query(Hardware).filter(Hardware.hardware_type == 'motherboard',
                                                     Hardware.spec.contains(socket))
    return render_template('index.html', hardwareList=motherboardList, pageTitle='Материнки на ' + socket.upper())


@app.route('/ram/<string:type>')
def ram(type):
    session = db_session.create_session()
    ramList = session.query(Hardware).filter(Hardware.hardware_type == 'ram', Hardware.spec.contains(type))
    return render_template('index.html', hardwareList=ramList, pageTitle='Оперативка ' + type.upper())


@app.route('/ps')
def ps():
    session = db_session.create_session()
    psList = session.query(Hardware).filter(Hardware.hardware_type == 'ps')
    return render_template('index.html', hardwareList=psList, pageTitle='БП-шки')


@app.route('/drive/<string:type>')
def drive(type):
    session = db_session.create_session()
    driveList = session.query(Hardware).filter(Hardware.hardware_type == type)
    return render_template('index.html', hardwareList=driveList, pageTitle='Накопители: ' + type.upper())


@app.route('/video')
def videoCard():
    return render_template('index.html', pageTitle='Тот кто делает бд долбоёб')


@app.route('/configurator')
def configurator():
    return render_template('configurator.html')


if __name__ == '__main__':
    app.run()
