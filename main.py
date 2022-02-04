from flask import Flask, render_template, request, jsonify
from data import db_session
from data.hardware import Hardware
from data.configurator import Configurator
from sqlalchemy import or_, func
import random

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'gayGard'
db_session.global_init('db/GDB.db')


@app.route('/')
def main():
    session = db_session.create_session()
    type_list = {
        'motherboard': {"name": "Материнские платы"},
        'cpu': {"name": "Процессоры"},
        'ram': {"name": "Оперативная память"},
        'gpu': {"name": "Видеокарты"},
    }
    hardware_list = {
        'motherboard': session.query(Hardware).order_by(func.random()).filter(Hardware.hardware_type == 'motherboard').limit(3),
        'cpu': session.query(Hardware).order_by(func.random()).filter(Hardware.hardware_type == 'cpu').limit(3),
        'ram': session.query(Hardware).order_by(func.random()).filter(Hardware.hardware_type == 'ram').limit(3),
        'gpu': session.query(Hardware).order_by(func.random()).filter(Hardware.hardware_type == 'gpu').limit(3)
    }
    return render_template('main.html', hardware_list=hardware_list, type_list=type_list)


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
        'Motherboard': {"name": "Материнскиая плата", "pic": 'motherboard.svg', 'h_name': 'motherboard'},
        'Cpu': {"name": "Процессор", "pic": 'cpu.svg', 'h_name': 'cpu'},
        'Ram': {"name": "Оперативная память", "pic": 'ram.svg', 'h_name': 'ram'},
        'Card': {"name": "Видеокарта", "pic": 'card.svg', 'h_name': 'gpu'},
        'HDD': {"name": "Накопитель", "pic": 'hdd.svg', 'h_name': 'hdd'},
        'PS': {"name": "Блок питания", "pic": 'power.svg', 'h_name': 'ps'},
        'Case': {"name": "Корпус", "pic": 'case.svg', 'h_name': 'case'},
    }

    session = db_session.create_session()
    hardware_list = {
        'motherboard': session.query(Hardware).filter(Hardware.hardware_type == 'motherboard'),
        'cpu': session.query(Hardware).filter(Hardware.hardware_type == 'cpu'),
        'ram': session.query(Hardware).filter(Hardware.hardware_type == 'ram'),
        'gpu': session.query(Hardware).filter(Hardware.hardware_type == 'gpu'),
        'hdd': session.query(Hardware).filter(or_(Hardware.hardware_type == 'hdd', Hardware.hardware_type == 'ssd')),
        'ps': session.query(Hardware).filter(Hardware.hardware_type == 'ps'),
        'case': session.query(Hardware).filter(Hardware.hardware_type == 'case')
    }

    return render_template('configurator.html', confList=confList, hardware_list=hardware_list)


@app.route('/saveCfg', methods=['POST'])
def save_cfg():
    data = request.get_json()
    session = db_session.create_session()
    configurator = Configurator()
    if data['name'] == '':
        configurator.name = 'Configuration' + str(random.randrange(0, 1000))
    else:
        configurator.name = data['name']
    configurator.price = data['price']
    configurator.motherboard = data['motherboard']
    configurator.cpu = data['cpu']
    configurator.ram = data['ram']
    configurator.gpu = data['gpu']
    configurator.drive = data['drive']
    configurator.ps = data['ps']
    configurator.case = data['case']
    hardware = session.query(Hardware).filter(Hardware.name == configurator.case)
    for i in hardware:
        configurator.picture = i.picture
    session.merge(configurator)
    session.commit()
    return jsonify({'result': 'success'})


@app.route('/configurations')
def all_configurations():
    session = db_session.create_session()
    configurations = session.query(Configurator)
    return render_template('configurations.html', pageTitle='Конфигурации', conf_list=configurations)


@app.route('/configuration/<int:id>')
def one_configuration(id):
    session = db_session.create_session()
    conf_list = session.query(Configurator).filter(Configurator.id == id)
    for hardware in conf_list:
        list = {
            'motherboard': hardware.motherboard,
            'cpu': hardware.cpu,
            'ram': hardware.ram,
            'gpu': hardware.gpu,
            'drive': hardware.drive,
            'ps': hardware.ps,
            'case': hardware.case,
            'price': hardware.price
        }

    hardware_list = {
        'motherboard': session.query(Hardware).filter(Hardware.name == list['motherboard']),
        'cpu': session.query(Hardware).filter(Hardware.name == list['cpu']),
        'ram': session.query(Hardware).filter(Hardware.name == list['ram']),
        'gpu': session.query(Hardware).filter(Hardware.name == list['gpu']),
        'drive': session.query(Hardware).filter(Hardware.name == list['drive']),
        'ps': session.query(Hardware).filter(Hardware.name == list['ps']),
        'case': session.query(Hardware).filter(Hardware.name == list['case'])
    }
    return render_template('configuration.html', conf_list=list, hardware_list=hardware_list)


@app.route('/search')
def search():
    session = db_session.create_session()
    s = request.args.get('s')
    hardware_list = session.query(Hardware).filter(Hardware.name.contains(s))
    return render_template('index.html', hardwareList=hardware_list, pageTitle='Поиск')


@app.route('/getprice', methods=["GET", "POST"])
def get_price():
    data = request.get_json()
    price_list = data['priceList']
    result = 0
    try:
        for price in price_list:
            result += int(''.join(price.split()[0:-1]))
    except TypeError:
        print('булат гомосексуалист')
    if 999 < result < 10000:
        result = [i for i in str(result)]
        result = f"{''.join(result[0:1])} {''.join(result[1: len(result)])}"
    elif 9999 < result < 100000:
        result = [i for i in str(result)]
        result = f"{''.join(result[0:2])} {''.join(result[2: len(result)])}"
    elif 99999 < result < 1000000:
        result = [i for i in str(result)]
        result = f"{''.join(result[0:3])} {''.join(result[3: len(result)])}"

    return jsonify({'price': result})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
