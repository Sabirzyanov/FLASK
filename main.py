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
    socket = ''.join([i for i in socket if i != ','])
    return render_template('index.html', hardwareList=motherboardList, pageTitle='Материнки на ' + socket.upper())


@app.route('/ram/<string:type>')
def ram(type):
    session = db_session.create_session()
    ramList = session.query(Hardware).filter(Hardware.hardware_type == 'ram', Hardware.spec.contains(type))
    return render_template('index.html', hardwareList=ramList, pageTitle='Оперативка ' + type.upper())


@app.route('/drive/<string:type>')
def drive(type):
    session = db_session.create_session()
    driveList = session.query(Hardware).filter(Hardware.hardware_type == type)
    return render_template('index.html', hardwareList=driveList, pageTitle='Накопители: ' + type.upper())


@app.route('/cooling/<string:type>')
def cooling(type):
    session = db_session.create_session()
    if type == 'сво':
        coolingList = session.query(Hardware).filter(Hardware.hardware_type == 'cooling', Hardware.spec.contains('СВО'))
    else:
        coolingList = session.query(Hardware).filter(Hardware.hardware_type == 'cooling', Hardware.spec.contains(type))
    return render_template('index.html', hardwareList=coolingList, pageTitle='Охлаждение: ' + type.upper())


@app.route('/ps')
def ps():
    session = db_session.create_session()
    psList = session.query(Hardware).filter(Hardware.hardware_type == 'ps')
    return render_template('index.html', hardwareList=psList, pageTitle='БП-шки')


@app.route('/case')
def case():
    session = db_session.create_session()
    psList = session.query(Hardware).filter(Hardware.hardware_type == 'case')
    return render_template('index.html', hardwareList=psList, pageTitle='Гробы для комплектующих')


@app.route('/gpu/<string:type>')
def videoCard(type):
    session = db_session.create_session()
    gpuList = session.query(Hardware).filter(Hardware.hardware_type == 'gpu', Hardware.name.contains(type))
    return render_template('index.html', hardwareList=gpuList, pageTitle='Видики')


@app.route('/configurator')
def configurator():
    confList = {
        'Motherboard': {"name": "Материнка", "pic": 'motherboard.svg', 'h_name': 'motherboard'},
        'Cpu': {"name": "Проц", "pic": 'cpu.svg', 'h_name': 'cpu'},
        'Ram': {"name": "Опера", "pic": 'ram.svg', 'h_name': 'ram'},
        'Card': {"name": "Видик", "pic": 'card.svg', 'h_name': 'gpu'},
        'HDD': {"name": "Накопитель", "pic": 'hdd.svg', 'h_name': 'hdd'},
        'PS': {"name": "БП", "pic": 'power.svg', 'h_name': 'ps'},
        'Case': {"name": "Гроб", "pic": 'case.svg', 'h_name': 'case'},
    }

    session = db_session.create_session()
    hardware_list = {
        'motherboard': session.query(Hardware).filter(Hardware.hardware_type == 'motherboard'),
        'cpu': session.query(Hardware).filter(Hardware.hardware_type == 'cpu'),
        'ram': session.query(Hardware).filter(Hardware.hardware_type == 'ram'),
        'gpu': session.query(Hardware).filter(Hardware.hardware_type == 'gpu'),
        'hdd': session.query(Hardware).filter(Hardware.hardware_type == 'hdd'),
        # 'ssd': session.query(Hardware).filter(Hardware.hardware_type == 'ssd'),
        'ps': session.query(Hardware).filter(Hardware.hardware_type == 'ps'),
        'case': session.query(Hardware).filter(Hardware.hardware_type == 'case')
    }

    return render_template('configurator.html', confList=confList, hardware_list=hardware_list)


if __name__ == '__main__':
    app.run()
