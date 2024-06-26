from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)