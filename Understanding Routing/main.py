from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/Champion")
def Champion():
    return "Champion!"

@app.route("/say/<name>")
def Hi(name):
    return f"Hi {name}!"

@app.route ("/repeat/<int:num>/<word>")
def word(num , word):
    return (word + " ")*num
    
if __name__=="__main__":
    app.run(debug=True,port=9000)