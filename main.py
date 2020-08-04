from flask import Flask, render_template

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'gayGard'


@app.route('/')
def main():
    return render_template('base.html')


@app.route('/cpu/all')
def allCpu():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
