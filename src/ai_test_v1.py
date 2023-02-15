import read_file
import json
from nltk.metrics import edit_distance
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    print("http method:"+request.method)
    if request.method == "POST":
        question = request.form["question"]
        print("question:"+question)
        return redirect(url_for("index", result=search(question)))
    result = request.args.get("result")
    return render_template("index.html",result=result)

'''
1. 对文本进行预处理：
'''
def search(input_text):
    text = read_file.read_data()
    # 计算相似度
    distances = [edit_distance(input_text, str(json.loads(item).get('title'))) for item in text]
    # 找到与用户输入最相似的已有数据
    min_distance = min(distances)
    most_similar = text[distances.index(min_distance)]
    print("most_similar：{}".format(most_similar))
    obj = json.loads(most_similar)
    print(obj.get('answer'))
    return obj.get('answer')

if __name__ == '__main__':
    app.run()

