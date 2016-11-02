from flask import Flask, render_template, redirect, url_for, abort
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

@app.route('/wandile-airliner-collection/boeing/737/')
def boeing_model_737():
    return render_template('737.html')

@app.route('/wandile-airliner-collection/boeing/747-400/')
def boeing_model_747():
    return render_template('747-400.html')

@app.route('/wandile-airliner-collection/boeing/757-200/')
def boeing_model_757():
    return render_template('757-200.html')

@app.route('/wandile-airliner-collection/boeing/767-300/')
def boeing_model_767():
    return render_template('767-300.html')

@app.route('/wandile-airliner-collection/boeing/777-300/')
def boeing_model_777():
    return render_template('777-300.html')

@app.route('/wandile-airliner-collection/boeing/787/')
def boeing_model_787():
    return render_template('787.html')

@app.route('/wandile-airliner-collection/airbus/')
def airbus():
    return render_template('airbus.html')

@app.route('/wandile-airliner-collection/airbus/a318/')
def airbus_model_a318():
    return render_template('a318.html')

@app.route('/wandile-airliner-collection/airbus/a321/')
def airbus_model_a321():
    return render_template('a321.html')

@app.route('/wandile-airliner-collection/airbus/a330-200/')
def airbus_model_a330():
    return render_template('a330-200.html')

@app.route('/wandile-airliner-collection/airbus/a340-600/')
def airbus_model_a340():
    return render_template('a340-600.html')

@app.route('/wandile-airliner-collection/airbus/a350/')
def airbus_model_a350():
    return render_template('a350.html')

@app.route('/wandile-airliner-collection/airbus/a380/')
def airbus_model_a380():
    return render_template('a380')

@app.route('/wandile-airliner-collection/bombardier/')
def bombardier():
    return render_template('bombardier.html')

@app.route('/wandile-airliner-collection/bombardier/crj200/')
def bombardier_model_crj200():
    return render_template('crj200.html')

@app.route('/wandile-airliner-collection/bombardier/crj900/')
def bombardier_model_crj900():
    return render_template('crj900.html')

@app.route('/wandile-airliner-collection/bombardier/cseries/')
def bombardier_model_cseries():
    return render_template('cseries.html')

@app.route('/wandile-airliner-collection/bombardier/dash8/')
def bombardier_model_dash8():
    return render_template('dash8.html')

@app.route('/wandile-airliner-collection/tupelov/')
def tupelov():
    return render_template('tupelov.html')

@app.route('/wandile-airliner-collection/tupelov/tu-204/')
def tupelov_model_tu204():
    return render_template('tu-204.html')

@app.route('/wandile-airliner-collection/tupelov/tu-154/')
def tupelov_model_tu154():
    return render_template('tu-154.html')

@app.route('/wandile-airliner-collection/embraer/')
def embraer():
    return render_template('embraer.html')

@app.route('/wandile-airliner-collection/embraer/erj145/')
def embraer_model_erj145():
    return render_template('erj145.html')

@app.route('/wandile-airliner-collection/embraer/e170/')
def embraer_model_e170():
    return render_template('e170.html')

@app.route('/wandile-airliner-collection/embraer/e190/')
def embraer_model_e190():
    return render_template('e190.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
