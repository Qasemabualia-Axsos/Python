from flask import Flask,render_template

app=Flask(__name__)

@app.route ("/")
def eight_eight():
    return render_template ('index.html',rows=8,cols=8,color1="black",color2="red")

@app.route ("/<int:cols>")
def eight_four(cols):
    return render_template ('index.html',rows=8,cols=cols,color1="black",color2="red")

@app.route("/<int:rows>/<int:cols>")
def custom_board(rows,cols):
    return render_template ('index.html',rows=rows,cols=cols,color1="black",color2="red")
    
@app.route("/<int:rows>/<int:cols>/<color1>/<color2>")
def alternating_colors(rows,cols,color1,color2):
    return render_template('index.html',rows=rows,cols=cols,color1=color1,color2=color2)
if __name__=="__main__":
    app.run(debug=True,port=7000)
