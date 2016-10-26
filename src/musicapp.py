from flask import Flask, render_template
app = Flask(__name__)

def layout():
    return render_template('index.html')

@app.route('/wandile-music-collection/')
def browse():
    return render_template('browse.hml')

@app.route('/wandile-music-collection/artists/')
def artists():
    return render_template('artists.html')

@app.route('/wandile-music-collection/albums/')
def albums():
    return render_template('albums.html')

@app.route('/wandile-music-collection/genres/')
def genres():
    return render_template('genres.html')

# @app.route('/')
# def root():
#     return render_template('base.html'), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
