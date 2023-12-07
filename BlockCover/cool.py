from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
  
def index():
    return render_template('index.html')

@app.route("/greet")
def greet():
    fname=request.args.get("fname", "world")
    return render_template("greet.html",name=fname)

if __name__=="__main__":
    app.run(debug=True)