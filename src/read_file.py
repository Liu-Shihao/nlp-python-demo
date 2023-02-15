import json

'''

{"qid":<qid>,"category":<category>,"title":<title>,"desc":<desc>,"answer":<answer>}
其中，category是问题的类型，title是问题的标题，desc是问题的描述，可以为空或与标题内容一致。
'''

def read_data():
    with open('/Users/liushihao/PycharmProjects/nlp-demo/data/baike_qa_valid.json', 'r') as file:
        content = file.readlines()
    return content

if __name__ == '__main__':
    content = read_data()
    for json_str in content:
        obj = json.loads(json_str)
        print(obj)