
# 多卡并行
from lmdeploy import pipeline, TurbomindEngineConfig, GenerationConfig

# backend_config = TurbomindEngineConfig(tp=2)
# pipe = pipeline('internlm/internlm2_5-7b-chat',
#                 backend_config = backend_config
#                 )
# response = pipe(['你好，介绍你自己'],['明天要'])
# print(response)

# 设置随机采样参数
backend_config = TurbomindEngineConfig(tp=2, cache_max_entry_count=0.3)
gen_config = GenerationConfig(
    top_p=0.3,
    top_k=40,
    temperature=0.3,
    max_new_tokens=512,
)
pipe = pipeline('internlm/internlm2_5-7b-chat',
                backend_config = backend_config,
                max_context_token_num=500
                )
response = pipe(['你好，介绍你自己'],['明天要'],
                gen_config=gen_config
                )
print(response)
