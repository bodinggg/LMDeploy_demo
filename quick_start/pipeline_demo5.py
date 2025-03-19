# 获取生成 token 最后一层的 hidden_states

from lmdeploy import pipeline, GenerationConfig

pipe = pipeline('/home/featurize/work/LLaMA-Factory/Qwen/Qwen2.5-3B-Instruct')

gen_config=GenerationConfig(output_last_hidden_state='generation',
                            max_new_tokens=10)
response = pipe(['你好，介绍你自己', '上海是'],
                gen_config=gen_config)
hidden_states = [x.last_hidden_state for x in response]
print(f'hidden_states is\n{hidden_states}')
