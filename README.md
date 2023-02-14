# spacy

在项目根目录下创建一个虚拟环境，并激活该虚拟环境：
```shell
#在项目根目录下创建一个虚拟环境，并激活该虚拟环境：
python -m venv .env
source .env/bin/activate

pip install -U pip setuptools wheel

pip install -U spacy

python3 -m spacy download zh_core_web_sm

python3 -m spacy download en_core_web_sm


#创建一个 requirements.txt 文件，列出所有需要的 Python 包：
numpy
pandas
scikit-learn



```

# python命令

```shell
#使用 pip 安装需要的包：
pip3 install -r requirements.txt

#检查安装的版本
pip3 show transformers

#安装特定版本的库
pip3 install transformers==<version>
```





# NLP框架

## Transformer
Transformer是一个Python库，由hug Face团队创建，用于使用各种预训练的Transformer模型完成各种自然语言处理(NLP)任务，如文本分类、语言生成、问题回答等。
它是一个构建在PyTorch上的高级API，提供了一种简单的方法来使用最新的最先进的NLP任务模型。
该库还支持来自OpenAI GPT系列、BERT、RoBERTa和许多其他模型的大量预训练模型。
由于易于使用、大量预先训练的模型和强大的社区支持，该库在最近获得了很大的人气。

# Python 基础知识
## pip&pip3
pip 和 pip3 都是 Python 包管理工具，它们的主要用途是帮助用户在 Python 环境中安装和管理第三方包。
主要的不同之处在于：
pip 通常默认对应 Python 2 的包管理工具；
pip3 通常默认对应 Python 3 的包管理工具。
所以如果你正在使用 Python 3，那么通常使用 pip3 来管理第三方包，而不是 pip。

## Python中如何管理项目结构
在 Python 中开发项目一般使用 pip 和 virtualenv 管理项目结构。
pip 是 Python 的包管理工具，允许你安装、升级、删除 Python 包，
而 virtualenv 则是一个 Python 虚拟环境管理工具，用于隔离各个项目的 Python 环境，避免全局安装的包与当前项目的包版本冲突。