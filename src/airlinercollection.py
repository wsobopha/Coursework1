from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def layout():
    return render_template('index.html')

@app.route('/body')
def body():
    manufacturer='boeing'
    models = ['737','747-400','757-200','767-300','777-300','787']
    return render_template('body.html',models=models,manufacturer=manufacturer)

@app.route('/wandile-airliner-collection/')
def browse():
    return render_template('browse.html')

@app.route('/wandile-airliner-collection/boeing/')
def boeing():
    models = ['737','747-400','757-200','767-300','777-300','787']
    images = ['737.jpg','747-400.jpg','757-200.jpg','767-300.jpg','777-300.jpg','787']
    return render_template('boeing.html', models=models,
    manufacturer='boeing',title='Boeing',images=images)

@app.route('/wandile-airliner-collection/airbus/')
def airbus():
    manufacturer = 'Airbus'
    return render_template('airbus.html')

@app.route('/wandile-airliner-collection/bombardier/')
def bombardier():
    manufacturer = 'Bombardier'
    models = ['crj200','crj900','cseries','dash8']
    return render_template('bombardier.html', models=models)

@app.route('/wandile-airliner-collection/tupelov/')
def tupelov():
    models = ['tu-204','tu-154','tu-144']
    return render_template('tupelov.html', models=models)

@app.route('/wandile-airliner-collection/embraer/')
def embraer():
    return render_template('embraer.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
