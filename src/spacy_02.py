import spacy

'''
为了完成NLP任务，我们一般需要对文本进行预处理。
预处理一般包括文本清洗、分词、去掉停用词、标准化和特征提取等（不过现在BERT横空出世，甚至可以不经过这些步骤）。
Spacy是这个领域内的一个比较领先好用的工业级处理库。

分词：Tokenizing
词形还原：Lemmatization  例如：is的词形被还原为了be，某些词的原形其实是一样的，处理的时候应该按照一样的文本处理
判断停用词：
'''
nlp = spacy.load('en_core_web_sm')

doc = nlp("Tea is healthy and calming, don't you think?")
for token in doc:
    print(token)

print(f"Token \t\tLemma \t\tStopword".format('Token', 'Lemma', 'Stopword'))
print("-"*40)
for token in doc:
    print(f"{str(token)}\t\t{token.lemma_}\t\t{token.is_stop}")

doc = nlp('help helped cup cups')
for token in doc:
    print(token.lemma_)