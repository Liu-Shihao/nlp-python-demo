import spacy

'''
文本预处理
zh_core_web_sm
1. 分词
2. 词性标注
2. 去除停用词
3. 词性还原
4. 命名实体识别
'''
#分词  并判断是否是停用词
nlp = spacy.load('zh_core_web_sm')
def token(str):
    doc = nlp(str)
    for token in doc:
        print('{} :  {}  :  {}  : {}'.format(token,token.pos_,token.lemma_,token.is_stop))
# 分句
def sentence(str):
    doc = nlp(str)
    for sent in doc.sents:
        print(sent)

# 命名实体识别：人名、地名、时间、地点
def namedEntityRecognition(str):
    doc = nlp(str)
    for ent in doc.ents:
        print('{}-{}'.format(ent, ent.label_))


if __name__ == '__main__':
    str = '你好，张三。明天上海的天气怎么样？我有100块，想去人民广场逛一逛'
    token(str)
    print("= "*20)
    sentence(str)
    print("= " * 20)
    namedEntityRecognition(str)