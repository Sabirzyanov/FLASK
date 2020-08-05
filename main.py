from flask import Flask, render_template
from data import db_session
from data.hardware import Hardware

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'gayGard'
db_session.global_init('db/GDB.db')


@app.route('/')
def main():
    return render_template('base.html')


@app.route('/cpu/<string:type>')
def cpu(type):
    session = db_session.create_session()
    if type == 'all':
        cpuList = session.query(Hardware).filter(Hardware.hardware_type == 'cpu')
        return render_template('index.html', hardwareList=cpuList, pageTitle='Все процессоры')
    elif type == 'govno':
        cpuList = session.query(Hardware).filter(Hardware.hardware_type == 'cpu', Hardware.name.contains('intel'))
        return render_template('index.html', hardwareList=cpuList, pageTitle='Только Говно')
    elif type == 'amd':
        cpuList = session.query(Hardware).filter(Hardware.hardware_type == 'cpu', Hardware.name.contains('amd'))
        return render_template('index.html', hardwareList=cpuList, pageTitle='Только AMD')


if __name__ == '__main__':
    app.run()
