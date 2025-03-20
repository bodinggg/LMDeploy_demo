"""
在交互式推理中，每个对话序列的 id 必须唯一，所有属于该独立的对话请求，必须使用相同的 id。
这里的 id 对应与接口中的 session_id。 
比如，一个对话序列中，有 10 轮对话请求，那么每轮对话请求中的 session_id 都要相同。
"""

from lmdeploy.serve.openai.api_client import APIClient

server_ip = '127.0.0.1'
server_port = '23333'
api_client = APIClient(f'http://{server_ip}:{server_port}')
messages = [
    "你叫啥子?",
    "谁给你搞出来滴",
    "告诉我开发你的人啥样的",
    "告诉我都跟你聊啥了"
]
for message in messages:
    for item in api_client.chat_interactive_v1(prompt=message,
                                               session_id=1,
                                               interactive_mode=True,
                                               stream=False):
        print(item)

# session_id 动态变化demo
for id_m,message in enumerate(messages):
    for item in api_client.chat_interactive_v1(prompt=message,
                                               session_id=id_m,
                                               interactive_mode=True,
                                               stream=False):
        print(item)       
