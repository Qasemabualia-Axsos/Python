from flask import Flask,redirect,render_template,request,session
import random
from datetime import datetime
app=Flask(__name__)
app.secret_key='secret_gold000'

Ranges={
        'farm':(10,20),
        'cave':(5,10),
        'house':(2,5),
        'casino':(-50,50)
    }
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'activities' not in session:
        session['activities']=[]
    return render_template('index.html',gold=session['gold'] , activities=session['activities'])

@app.route('/process_money' , methods=['POST'])
def procesMoney():
    ranges=request.form['ranges']
    low,high=Ranges[ranges]
    gold_earned=random.randint(low,high)
    session['gold']+=gold_earned

    time=datetime.now().strftime("%Y/%m/%d %I:%M %p")
    if gold_earned >=0:
        color='green'
        msg=f"Earned {gold_earned} golds from the {ranges}! ({time})"
    else:
        color='red'
        msg=f'Entered a {ranges} and lost {abs(gold_earned)} golds ....{time}'
    
    session["activities"].insert(0, {"msg": msg, "color": color})

    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')

if __name__=='__main__':
    app.run(debug=True,port=8006)