"""
以下代码是通过 openai 包使用 v1/chat/completions 服务的例子。
"""

from openai import OpenAI
client = OpenAI(
    api_key='your openai key',
    base_url="http://127.0.0.1:23333/v1"
)
model_name = client.models.list().data[0].id
response = client.chat.completions.create(
  model=model_name,
  messages=[
    {"role": "system", "content": "你是个小可爱"},
    {"role": "user", "content": " 讲个笑话给我"},
  ],
    temperature=0.8,
    top_p=0.8
)
print(response)
