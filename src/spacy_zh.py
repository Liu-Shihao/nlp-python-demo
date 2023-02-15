import spacy

# 加载预训练模型
nlp = spacy.load('zh_core_web_sm')

def deal_with(text):
    # 对文本进行分词、分句、词性标注、命名实体识别等处理
    doc = nlp(text)
    keywords = []
    # 遍历每个分句
    for sent in doc.sents:
        # 遍历每个词
        for token in sent:
            # 打印每个词的文本、词性标注、命名实体标注
            # print(token.text, token.pos_, token.ent_type_ if token.ent_type_ else "-")
            # 如果词性是名词或形容词，将其添加到关键词列表中
            if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
                keywords.append(token.text)
    # 打印关键词列表
    print(keywords)
if __name__ == '__main__':
    text = '文本分词是自然语言处理中的一个基础任务，它将一段文本分解成一个一个的单词或词汇单元，这些单词或词汇单元被称为“词汇”，并且对于很多NLP任务来说都是必要的预处理步骤。'
    deal_with(text)