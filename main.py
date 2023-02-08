from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1> Hello world! <h1>"

@app.route('/salom')
def salom():
    return "<h1>salom qalaysiz <h1>"


if __name__ == '__main__':
    app.run()