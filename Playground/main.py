from flask import Flask,render_template
app=Flask(__name__)

@app.route("/play")
def play():
    return render_template ("index.html",title="Play ground 1")

@app.route("/play/<x>")
def play_x(x):
    x=int(x)
    return render_template ("page2.html",title="play ground 2",num=x)

@app.route("/play/<x>/<color>")
def play_color(x,color):
    x=int(x)
    return render_template("page3.html",num=x ,color=color)
    
if __name__=="__main__":
    app.run(debug=True,port=9000)