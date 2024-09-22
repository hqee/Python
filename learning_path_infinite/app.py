from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World!!!</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"HALOO {name}"

@app.route('/add/<int:nomor1>/<int:nomor2>')
def add(nomor1, nomor2):
    return f"{nomor1} + {nomor2} = {nomor1 + nomor2}"

@app.route('/params')
def params():
    greeting = request.args['greet']
    name = request.args['name']

    return f'{greeting}, {name}'

@app.route('/html')
def html():
    list_data = [10,20,2,10]
    return render_template(template_name_or_list='index.html', list_data=list_data)

@app.route('/other')
def other():
    return render_template(template_name_or_list='other.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1234, debug=True)