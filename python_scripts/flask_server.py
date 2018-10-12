from flask import Flask, jsonify, request
import math

app = Flask(__name__)


@app.route("/test_get", methods=['GET'])
def test1():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    prod = num1*num2
    sum = num1+num2
    gcd = math.gcd(num1,num2)
    if(gcd!=0):
        lcm = prod/gcd
    else:
        lcm = 0

    res = {"product" : prod , "sum" : sum, "gcd" : gcd ,"lcm" : lcm}

    return jsonify(res)

@app.route("/test_post", methods=['POST'])
def test2():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    prod = num1*num2
    sum = num1+num2
    gcd = math.gcd(num1,num2)
    if(gcd!=0):
        lcm = prod/gcd
    else:
        lcm = 0

    res = {"product" : prod , "sum" : sum, "gcd" : gcd ,"lcm" : lcm}

    return jsonify(res)



if __name__ == '__main__':
    app.run(debug=True, port=1234)
