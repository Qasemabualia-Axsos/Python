from flask import Flask,render_template,request,redirect,session

app=Flask(__name__)

app.secret_key='keep_it_secret_keep_it_safe'

@app.route("/")
def counter():
    if "count" in session:
        session['count']+=1
    else:
        session['count']=0
    return render_template('index.html',count=session['count'],num=0)

@app.route("/destroy_session",methods=['POST','GET'])
def destroy():
    session.clear()
    return redirect('/')

@app.route("/increase_by_2",methods=['POST','GET'])
def increase_by_2():
    session['count']=session.get('count',0)+1
    return redirect('/')


@app.route("/increase_by_user", methods=['POST'])
def increase_by_user():
    add=int(request.form['add'])
    session['count']=session.get('count',0)+add
    return render_template('index.html' ,count=session['count'])



@app.route('/increase_by_user/<int:num>',methods=['POST'])
def increase_by_user_by_num(num):
    session['count']=session.get('count',0)+num
    return render_template('index.html' ,count=session['count'],num=0)


if __name__=='__main__':
    app.run(debug=True,port=8002)