# # LLM
# import lmdeploy
# pipe = lmdeploy.pipeline('/home/featurize/work/LLaMA-Factory/Qwen/Qwen2.5-3B-Instruct')
# response = pipe(['hi','say this is a test'])
# print(response)

# VLM
from lmdeploy.vl import load_image
from lmdeploy import pipeline, TurbomindEngineConfig, ChatTemplateConfig
pipe = pipeline('liuhaotian/llava-v1.5-7b',
                backend_config=TurbomindEngineConfig(session_len=8192),
                chat_template_config=ChatTemplateConfig(model_name='llava'))
im = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/demo/resources/human-pose.jpg')
response = pipe([('描述这个图片', [im])])
print(response)
