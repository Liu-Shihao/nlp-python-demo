from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

'''


'''
@app.route('/',methods=['GET','POST'])
def index():
    print("http method:"+request.method)
    if request.method == "POST":
        question = request.form["question"]
        print("question:"+question)
        return redirect(url_for("index", result="I'm your personal assistant. You can call me Jarvis."))
    result = request.args.get("result")
    return render_template("index.html",result=result)

if __name__ == '__main__':
    app.run()
