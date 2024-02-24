from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/about')
def about():
    return "Hello"

if __name__ == "__main__":
    app.run()