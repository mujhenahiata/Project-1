from flask import Flask,request,render_template
#by default 5000 port
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to flask"

@app.route('/cal',methods=["GET"])
def math_ops():
    ops=request.json["ops"]
    a=request.json["number_1"]
    b=request.json["number_2"]
    if ops =='+':
        print("add")
        return a+b
    elif ops =='-':
        print("sub")
        return a-b
    elif ops =='*':
        print("mul")
        return a*b
    elif ops =='/':
        print("div")
        return a/b
    else :
        print("enter a valid ops")
    


print(__name__)
if __name__=='__main__':
    app.run()