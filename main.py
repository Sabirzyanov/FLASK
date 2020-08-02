from flask import Flask, render_template

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'gayGard'


@app.route('/')
def index():
    return render_template('base.html', title='GayPC')


if __name__ == '__main__':
    app.run()
