# 计算 ppl-Perplexity
# 是度量一个语言模型 M 产生的序列与真实分布（ground truth）之间的差异；
# Perplexity的值越小，表示这个语言模型性能越好

from transformers import AutoTokenizer
from lmdeploy import pipeline


model_repoid = '/home/featurize/work/LLaMA-Factory/Qwen/Qwen2.5-3B-Instruct'
pipe = pipeline(model_repoid)
tokenizer = AutoTokenizer.from_pretrained(model_repoid, trust_remote_code=True)
messages = [
   {"role": "user", "content": "你好，介绍你自己"},
]
# apply_chat_template:将带有"role"和"content"键的字典列表转换为标记列表ids。
# 此方法旨在用于聊天模型，并将读取tokenizer的chat_template属性
# 确定转换时要使用的格式和控制令牌。
input_ids = tokenizer.apply_chat_template(messages)

# logits is a list of tensor
logits = pipe.get_logits(input_ids)
print(logits)

# ppl is a list of float numbers
ppl = pipe.get_ppl(input_ids)
print(ppl)
