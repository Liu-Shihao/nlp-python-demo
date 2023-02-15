from nltk.metrics import edit_distance

'''
这是一个简单的示例，在实际应用中，您可能需要更多复杂的算法，
例如模糊匹配、相似性分析等，但这些都是 NTLK 库提供的功能，您可以通过查看官方文档了解更多详情。
'''
# 已有数据，表示为一个列表
data = ['dog', 'cat', 'mouse', 'horse']

# 用户输入的文本
input_text = 'cats'

# 计算用户输入和已有数据之间的编辑距离
# 如果编辑距离小，说明相似度高
distances = [edit_distance(input_text, item) for item in data]

# 找到与用户输入最相似的已有数据
min_distance = min(distances)
most_similar = data[distances.index(min_distance)]

# 打印出相似度最高的已有数据
print('The most similar data is:', most_similar)
