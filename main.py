from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/primeira')

def primeira():
    return render_template('primeira.html')

@app.route('/segunda')

def segunda():
    return render_template('segunda.html')

@app.route('/terceira')

def terceira():
    return render_template('terceira.html')

@app.route('/quarta')

def quarta():
    return render_template('quarta.html')

if __name__ == '__main__':
    app.run(debug=True)