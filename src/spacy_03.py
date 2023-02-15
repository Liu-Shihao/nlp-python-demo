import spacy
from spacy import displacy

nlp=spacy.load('en_core_web_sm')
doc=nlp('Weather is good, very windy and sunny. We have no classes in the afternoon.')

# 分词
def tokenTest():
    for token in doc:
        print(token)
#分句
def sentTest():
    for sent in doc.sents:
        print(sent)
#词性
def tokenPosTest():
    for token in doc:
        print('{}-{}'.format(token,token.pos_))

#命名实体识别
def entsLabelTest():
    doc = nlp('I went to Beijing where I met my old friend Jack from uni.')
    for ent in doc.ents:
        print('{}-{}'.format(ent, ent.label_))
    displacy.render(doc, style='ent', jupyter=False)

if __name__ == '__main__':
    tokenTest()
    print("-=" * 10)
    sentTest()
    print("-=" * 10)
    tokenPosTest()
    print("-=" * 10)
    entsLabelTest()










