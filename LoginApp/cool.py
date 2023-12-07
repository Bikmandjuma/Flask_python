from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    
    if request.method=="GET":
        return render_template('index.html')
    
    elif request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        if username == "bikman123@" and password == "password123":
            return render_template('Sign.html',name=request.args.get("Bikman"))
        else:
            return render_template('index.html',wrong_credential=request.args.get("Wrong credentials !"))

if __name__=="__main__":
    app.run(debug=True) 