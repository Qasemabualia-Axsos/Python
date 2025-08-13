from datetime import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    date=datetime.now()
    name=request.form.get('name')
    id=request.form.get('id')
    number=request.form.get('zero')
    number1=request.form.get('one')
    number2=request.form.get('two')
    count=number+number1+number2
    print (f"{name} for {count} fruit ")
    return render_template("checkout.html",name=name,id=id,number=int(number),number1=int(number1),number2=int(number2),date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True,port=8001)    