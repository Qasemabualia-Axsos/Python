import random
from flask import Flask,render_template,redirect,request,session

app=Flask(__name__)
app.secret_key='secret123'


@app.route('/',methods=['POST','GET'])
def inex():
    if 'num' not in session:
       session ['num']=random.randint(1,100)
    if request.method=='POST':
        guess=request.form.get('guess')
        if not guess:
            return render_template('index.html')

        guess=int(guess)
        num=session['num']
        if guess < num:
            return render_template('/too_low.html' )

        elif guess > num:
            return render_template('/too_high.html')
        else:
            number=num
            session.pop('num')
            return render_template('/correct.html', number=number)
        
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True,port=8005)