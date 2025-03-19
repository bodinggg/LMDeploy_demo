# 获取生成token的logits
from lmdeploy import pipeline, GenerationConfig

pipe = pipeline('/home/featurize/work/LLaMA-Factory/Qwen/Qwen2.5-3B-Instruct')

gen_config=GenerationConfig(output_logits='generation',
                            max_new_tokens=10)
response = pipe(['你好，介绍你自己', '上海是'],
                gen_config=gen_config)
logits = [x.logits for x in response]
print(f'logits is \n {logits}')
