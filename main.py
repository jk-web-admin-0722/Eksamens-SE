
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

@app.route('/data')
def data():
   return render_template('data.html')

@app.route('/dataDB')
def dataDB():
   return render_template('dataDB.html')

@app.route('/kontakti', methods = ['GET', 'POST'])
def kontakti():
    msg = ""
    if request.method == 'POST':
        firstname = request.form.get('first-name')
        lastname =  request.form.get('last-name')
        email = request.form.get('email')
        text = request.form.get('text')
        # rindina prieks CSV
        line = f"{firstname},{lastname},{email},{text}\n"

        #rindina prieks DB ieraksta
        dbLine = {'vards':firstname, 'uzvards':lastname, 'epasts':email, 'zina':text}

        #rakstam iekšā CSV failā
        with open("zinas.csv", "a", encoding="utf-8") as f:
            f.write(line)

        #rakstam iekšā Datubāzē
        pievienotDatus(dbLine)
        
        msg = "Paldies! Jūsu ziņa saņemta!"

    return render_template('kontakti.html', message = msg)

if __name__ == "__main__":
   app.run(debug = True)



