from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
  
def index():
    # call a urlargument in html file as name_blueprint

    # if "name" in request.args:
    #     name=request.args["name"]
    # else:
    #     name="World"

    # this is also a calling a url blueprint name
    
    name=request.args.get("name")
    if name == None:
        name="World"

    return render_template('index.html',MyName=name)

if __name__=="__main__":
    app.run(debug=True)