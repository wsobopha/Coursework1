from flask import Flask, render_template, redirect, url_for, abort, request

app = Flask(__name__)

@app.route("/wandile-airliner-collection/", methods=['POST','GET'])
def browse():
    if request.method == 'POST':
      if 'one' in request.form:
        number_of_engines = request.form.getlist('engines')
        engines = number_of_engines[0]
        print engines
        return render_template('browse.html',engines=engines)
      elif 'two' in request.form:
        number_of_seats = request.form.getlist('seats')
        seats = number_of_seats[0]
        print seats
        return render_template('browse.html',seats=seats)
      elif 'three' in request.form:
        nautical_range = request.form.getlist('range')
        range = nautical_range[0]
        print range
        return render_template('browse.html',range=range)
      elif 'four' in request.form:
        airline_operators = request.form.getlist('operators')
        operators = airline_operators[0]
        print operators
        return render_template('browse.html',operators=operators)
      elif 'five' in request.form:
        body_size = request.form.getlist('body')
        body = body_size[0]
        print body
        return render_template('browse.html',body=body)
      

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

@app.errorhandler(404)
def page_not_found(error):
		return render_template('404page.html'), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
