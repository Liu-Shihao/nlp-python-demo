

from transformers import pipeline

'''

'''


def test1():
    # Allocate a pipeline for sentiment-analysis
    classifier = pipeline('sentiment-analysis')
    # Classify text
    print(classifier('I am a fan of KDnuggets, its useful content, and its helpful editors!'))


def test2():
    # Allocate a pipeline for question-answering
    question_answerer = pipeline('question-answering')
    # Ask a question
    answer = question_answerer({
        'question': 'Where is KDnuggets headquartered?',
        'context': 'KDnuggets was founded in February of 1997 by Gregory Piatetsky in Brookline, Massachusetts.'
    })
    # Print the answer
    print(answer)


if __name__ == '__main__':
    test2()