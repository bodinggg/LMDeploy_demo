# pytorch推理引擎的使用
# 使用lora微调
from lmdeploy import pipeline, GenerationConfig, PytorchEngineConfig

# adapters 加载lora训练配置：
# adapters (dict): The path configs to lora adapters.
backend_config = PytorchEngineConfig(session_len=2048,
                                     adapters=dict(lora_name_1='chenchi/lora-chatglm2-6b-guodegang'))
gen_config = GenerationConfig(top_p=0.8,
                              top_k=40,
                              temperature=0.8,
                              max_new_tokens=1024)
pipe = pipeline('THUDM/chatglm2-6b',
                backend_config=backend_config)
prompts = [[{
    'role': 'user',
    'content': '您猜怎么着'
}]]
response = pipe(prompts, gen_config=gen_config, adapter_name='lora_name_1')
print(response)
