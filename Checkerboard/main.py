from flask import Flask,render_template

app=Flask(__name__)

@app.route ("/")
def eight_eight():
    return render_template ('index.html',rows=8,cols=8)

@app.route ("/<int:cols>")
def eight_four(cols):
    return render_template ('index.html',rows=8,cols=cols)

@app.route("/<int:rows>/<int:cols>")
def custom_board(rows,cols):
    return render_template ('index.html',rows=rows,cols=cols)

if __name__=="__main__":
    app.run(debug=True,port=7000)