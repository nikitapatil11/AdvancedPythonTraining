from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1> Hello World </h1>'

# dynamic route
# http:127.0.0.1/Ayush
# Hello Ayush

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)