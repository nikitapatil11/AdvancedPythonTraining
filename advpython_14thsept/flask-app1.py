from flask import *
app=Flask(__name__)

# income=[
#     {"description":"salary","amount":5000}
# ]
# @app.route("/income")
# def get_income():
#     return jsonify(income)
# @app.route("/income",methods=["POST"])
# def add_income():
#     income.append(request.get_json())
#     return  'created',201

stock={
    "fruit":
        {
        "apple":100,
        "banana":45,
        "cherry":1000
},
    "vegetable":
        {

        }
}
@app.route("/stock")
def get_stock():
    res=make_response(jsonify(stock),200)
    return res
@app.route("/stock/<collection>")
def get_collection(collection):
        if collection in stock:
            return make_response(jsonify(stock[collection]),200)

        return make_response(jsonify({"error":"not found"}),404)
@app.route("/stock/<collection>/<member>")
def get_member(collection,member):
    if collection in stock:
        member=stock[collection].get(member)
        if member:
            return make_response(jsonify(member),200)
        return make_response(jsonify({"error":"not found"}),404)
    return make_response(jsonify({"error":"not found"}),404)
@app.route("/stock/<collection>",methods=["PUT"])
def put_collection(collection):
    req=request.get_json()
    if collection in stock:
        stock[collection].update(req)
        return make_response(jsonify({"msg": "collection updated"}), 200)


    if collection in stock:
        stock[collection]=req
        return make_response(jsonify({"msg":"collection updated"}),200)
    stock[collection]=req
    return make_response(jsonify({"msg":"collection created"}),201)
@app.route("/stock/<collection>",methods=["DELETE"])
def del_collection(collection):
    if collection in stock:
        del stock[collection]
        return make_response(jsonify({"msg":"deleted"}),200)
    return make_response(jsonify({"msg":"no records to delete"}))
@app.route("/stock/<collection>/<member>",methods=["DELETE"])
def del_member(member,collection):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            return make_response(jsonify({"msg": "deleted"}), 200)
        return make_response(jsonify({"msg": "no member to delete"}))
    return make_response(jsonify({"msg": "no collection to delete"}))
if __name__=='__main__':
    app.run(debug=True)
