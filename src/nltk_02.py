import nltk
from nltk.stem import SnowballStemmer

'''
languages = (
        "arabic",
        "danish",
        "dutch",
        "english",
        "finnish",
        "french",
        "german",
        "hungarian",
        "italian",
        "norwegian",
        "porter",
        "portuguese",
        "romanian",
        "russian",
        "spanish",
        "swedish",
    )
'''

# 初始化Snowball词干提取器，选择适当的语言（例如英语）
stemmer = SnowballStemmer('english')

# 定义要进行词干提取的单词列表
words = ['running', 'runs', 'runner', 'ran', 'fairly']

# 使用Snowball词干提取器将单词列表转换为它们的词干形式
stemmed_words = [stemmer.stem(word) for word in words]

# 打印输出结果
print(stemmed_words)
