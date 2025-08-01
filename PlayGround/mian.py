from flask import Flask,render_template

app=Flask(__name__)

@app.route("/play")
def first():
    return render_template("index.html",num=3,color="#9fc5f8")

@app.route("/play/<x>")
def second(x):
    return render_template ("index.html",num=int(x),color="#9fc5f8")

@app.route("/play/<x>/<color>")
def third(x,color):
    return render_template ("index.html",num=int(x),color=color)

if __name__==("__main__"):
    app.run(debug=True,port=9000)
