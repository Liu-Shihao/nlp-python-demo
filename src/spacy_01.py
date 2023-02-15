import spacy

from spacy.lang.en.stop_words import STOP_WORDS
'''
spaCy主要功能包括分词、词性标注、词干化、命名实体识别、名词短语提取等等。
'''

nlp = spacy.load("en_core_web_sm")
sample = u"I can't imagine spending $3000 for a single bedroom apartment in N.Y.C."
doc = nlp(sample)
# Print out tokens

print("Tokens:\n=======")
for token in doc:
    print(token)
# Identify stop words
print("Stop words:\n===========")
for word in doc:
    if word.is_stop == True:
        print(word)
# POS tagging
print("POS tagging:\n============")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
# Print out named entities
print("Named entities:\n===============")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)