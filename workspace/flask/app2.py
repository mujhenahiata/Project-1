from flask import Flask,request,render_template,jsonify

#by default 5000 port
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to flask"

@app.route('/cal',methods=["GET"])
def math_ops():
    ops=request.json["ops"]
    a=int(request.json["number_1"])
    b=int(request.json["number_2"])
    if ops =='+':
        print("add")
        return jsonify((a+b))
    elif ops =='-':
        print("sub")
        return jsonify((a-b))
    elif ops =='*':
        print("mul")
        return jsonify((a*b))
    elif ops =='/':
        print("div")
        return jsonify((a/b))
    else :
        print("enter a valid ops")
    


print(__name__)
if __name__=='__main__':
    app.run(debug=True)