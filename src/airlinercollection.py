from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def layout():
    return render_template('index.html')

@app.route('/body')
def body():
    return render_template('body.html')

@app.route('/wandile-airliner-collection/')
def browse():
    return render_template('browse.html')

@app.route('/wandile-airliner-collection/boeing/')
def boeing():
    return render_template('boeing.html')

@app.route('/wandile-airliner-collection/airbus/')
def airbus():
    return render_template('airbus.html')

@app.route('/wandile-airliner-collection/bombardier/')
def bombardier():
    return render_template('bombardier.html')

@app.route('/wandile-airliner-collection/tupelov/')
def tupelov():
    return render_template('tupelov.html')

@app.route('/wandile-airliner-collection/embraer/')
def embraer():
    return render_template('embraer.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
