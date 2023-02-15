import gensim
import numpy as np

'''
生成词向量是一项常见的自然语言处理任务，常用的工具包括word2vec和GloVe。
在此示例中，gensim包用于加载和访问预训练的word2vec模型。
首先，我们从文件中加载模型，并使用model[word]来获取单个词的词向量，或使用model[word]获取多个词的词向量。
词向量通常是具有数百维的实值向量，每个维度代表词的某个语义特征。
通过比较不同的词的向量，我们可以计算它们之间的相似度或距离，进而进行各种自然语言处理任务，如聚类、分类和翻译等。
'''
# Load the pre-trained word2vec model
model = gensim.models.KeyedVectors.load_word2vec_format('path/to/word2vec/model', binary=True)

# Get the vector for a single word
vector = model['apple']

# Get the vectors for multiple words
vectors = np.array([model[word] for word in ['apple', 'banana', 'orange']])
