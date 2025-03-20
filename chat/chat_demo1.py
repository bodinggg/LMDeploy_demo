# /v1/chat/completions 接口
from lmdeploy.serve.openai.api_client import APIClient
server_ip = '0.0.0.0'
server_port = '23333'
api_client = APIClient(f'http://localhost:{server_port}/')
model_name = api_client.available_models[0]
messages = [{"role": "user", "content": "Say this is a test!"}]
for item in api_client.chat_completions_v1(model=model_name, messages=messages):
    print(item)
