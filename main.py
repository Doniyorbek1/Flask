from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     r = request.args
#     name = r["name"]
#     data = {
#         'apple': 13,
#         'banana': 15,
#         'orange': 18
#     }
#     return {name: data.get(name, "not found")}

@app.route('/get_sum')
def get_summ():
    r = request.args
    a = int(r['a'])
    b = int(r['b'])
    return {"sum":a+b}


if __name__ == '__main__':
    app.run()