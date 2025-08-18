from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    id=request.form['student_id']
    num1=request.form['strawberry']
    num2=request.form['raspberry']
    num3=request.form['apple']
    return render_template("checkout.html",first_name=first_name,last_name=last_name,id=id,num1=int(num1),num2=int(num2),num3=int(num3))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True,port=8008)    