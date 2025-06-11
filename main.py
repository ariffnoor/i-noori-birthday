from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/cake')
def cake():
    return render_template("cake.html")

@app.route('/letter')
def letter():
    return render_template("letter.html")

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cake')
def cake():
    return render_template('cake.html')

@app.route('/letter')
def letter():
    return render_template('letter.html')

if __name__ == '__main__':
    app.run()
