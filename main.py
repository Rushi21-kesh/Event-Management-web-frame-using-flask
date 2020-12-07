from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def frame():
    return render_template('frame.html')

#header part
@app.route("/head")
def head():
    return render_template('head.html')


# containt 
@app.route('/0')
def about():
    return render_template('0.html')

@app.route('/1')
def login():
    return render_template('1.html')

@app.route('/2')
def forgot():
    return render_template('2.html')

@app.route('/3')
def registration():
    return render_template('3.html')

@app.route('/4')
def bookorder():
    return render_template('4.html')

@app.route('/5')
def contact():
    return render_template('5.html')

@app.route('/6')
def gallery():
    return render_template('6.html')

# Footer part

@app.route("/img")
def img():
    return render_template('img.html')

@app.route('/formal')
def formal():
    return render_template('formal.html')

@app.route('/informal')
def informal():
    return render_template('informal.html')

@app.route('/venue')
def venue():
    return render_template('venue.html')

#Formal part

@app.route('/sc')
def sc():
    return render_template('sc.html')

@app.route('/bm&sm')
def bmsm():
    return render_template('bm&sm.html')

@app.route('/appre')
def appre():
    return render_template('appre.html')

@app.route('/pl')
def pl():
    return render_template('pl.html')

#line bar menu 
@app.route('/about')
def aboutpro():
    return render_template('about.html')

@app.route('/login')
def loginpro():
    return render_template('sign.html')

@app.route('/forgot')
def forgotpro():
    return render_template('forgot.html')

@app.route('/new')
def registrationpro():
    return render_template('new.html')

@app.route('/book')
def bookpro():
    return render_template('book.html')

@app.route('/contact')
def contactpro():
    return render_template('contact.html')

@app.route('/gallery')
def gallerypro():
    return render_template('gallery.html')

app.run(debug=True)