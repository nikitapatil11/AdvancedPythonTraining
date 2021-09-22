from flask import Flask, jsonify, request

app = Flask(__name__)

income = [
    {"description": "salary", "amount": 5000}
]


@app.route("/income")
def get_incomes():
    return jsonify(income)


@app.route("/incomes", methods=["POST"])
def add_income():
    income.append(request.get_json())
    return 'Create', 201


if __name__ == '__main__':
    app.run(debug=True, port=5001)
