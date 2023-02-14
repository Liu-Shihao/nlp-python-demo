from flask import Flask, request

'''
创建Flask应用程序实例
__name__是一个特殊变量，当程序作为主程序运行时它的值是"__main__"，如果是从模块中被调用则为模块名字。
Flask是Flask库的核心类，这个语句创建了一个名为app的Flask应用程序实例，可以使用这个实例来设置、配置和启动web应用程序。
'''
app = Flask(__name__)

# openai.api_key = os.getenv("OPENAI_API_KEY")
'''
Flask是一个轻量级的Web框架，用于快速构建Web应用程序。
它是用Python语言开发的，提供了简洁的语法和功能强大的插件，使得开发人员能够快速构建出自己的Web应用程序。
Flask有一个很好的文档和活跃的社区，因此开发人员可以很容易地了解如何使用它并得到帮助。
在命令行中，启动该程序并打开浏览器以访问 http://localhost:5000/，将显示 "Hello, World!"。 
如果你想打招呼，请访问 http://localhost:5000/greet?name=John。
'''

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', '')
    response = "Hello " + name
    return response

'''
Flask 默认端口是5000，可以在 app.run(port=8000) 自定义端口号
'''
if __name__ == '__main__':
    app.run()
