from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/sakums')
def home():
   return render_template('sakums.html')

@app.route('/etron')
def etron():
   return render_template('etron.html')
   
@app.route('/tesla')
def tesla():
   return render_template('tesla.html')

@app.route('/fiat')
def fiat():
   return render_template('fiat.html')

@app.route('/i3')
def i3():
   return render_template('i3.html')

@app.route('/id3')
def id3():
   return render_template('id3.html')

@app.route('/leaf')
def leaf():
   return render_template('leaf.html')

@app.route('/zoe')
def zoe():
   return render_template('zoe.html')


if __name__ == "__main__":
   app.run(debug = True)