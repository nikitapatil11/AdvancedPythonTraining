# HTTP Response Code RFC 1656

# 1.x
# 2.x
# 3.x
# 4.x
# 5.x

from flask import Flask

app = Flask(__name__)


@app.route("/create/account", method=["post"])
def index():
    return '<h1> Hello World </h1>'


if __name__ == '__main__':
    app.run(debug=True)
