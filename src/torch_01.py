import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
'''
这段代码是一个使用Python语言和Transformers库生成文本的示例。
首先，它导入了Torch库和Transformers库中的GPT2Tokenizer和GPT2LMHeadModel。
然后，它使用GPT2Tokenizer从预训练模型中加载了一个tokenizer，并使用GPT2LMHeadModel从预训练模型中加载了一个模型。
接下来，它使用tokenizer对提示文本进行编码，并通过调用模型生成文本。它使用softmax函数将最后一个位置的logits转换为概率分布，然后使用torch.multinomial从这个分布中采样下一个单词的ID。
最后，它使用tokenizer将生成的ID序列解码为文本，并将生成的文本打印出来。
'''

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Encode the prompt and generate text
prompt = "Once upon a time"
input_ids = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)  # Batch size 1
outputs = model(input_ids, labels=input_ids)
loss, logits = outputs[:2]

# Sample the next word
probabilities = torch.nn.functional.softmax(logits[0, -1], dim=0)
next_token_id = torch.multinomial(probabilities, num_samples=1).item()
generated = tokenizer.decode(input_ids.tolist()[0] + [next_token_id])

# Print the generated text
print(generated)
