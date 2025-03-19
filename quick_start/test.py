import lmdeploy
from lmdeploy import pipeline, TurbomindEngineConfig, PytorchEngineConfig, GenerationConfig
# 离线批处理
# LLM推理
#pipelin默认TurboMind引擎
# pipeline支持本地模型路径调用
pipe = lmdeploy.pipeline("/home/featurize/work/LLaMA-Factory/Qwen/Qwen2.5-3B-Instruct")
# response = pipe(["介绍你自己","上海是"])
# print(response)
# 可以手动选择一个引擎


# print(f'选择TurboMind引擎')
# pipe = pipeline('/home/featurize/work/LLaMA-Factory/Qwen/Qwen2.5-3B-Instruct',
#                 backend_config=TurbomindEngineConfig(
#                     max_batch_size=32,
#                     enable_prefix_caching=True,
"""
cache_max_entry_count显著影响GPU内存占用，表示加载模型权重后K/V缓存占用的空闲GPU内存的比例。默认值是0.8
K/V缓存分配方式是一次性申请，重复性使用。
如果内存不足（OOM），考虑降低cache_max_entry_count的数值。
"""
#                     cache_max_entry_count=0.8,    
#                     session_len=8192,
#                 )
#                 )

# print(f'选择PytorchEngine引擎')
# pipe = pipeline('/home/featurize/work/LLaMA-Factory/Qwen/Qwen2.5-3B-Instruct',
#                 backend_config=PytorchEngineConfig(
#                     max_batch_size=32,
#                     enable_prefix_caching=True,
#                     cache_max_entry_count=0.8,
#                     session_len=8192,
#                 )
#                 )

prompts = ["介绍你自己","上海是"]
response = pipe(
    prompts=prompts,
    gem_config = GenerationConfig(
        max_new_tokens=1024,
        top_p=0.8,
        top_k=40,
        temperature=0.6
    )
)

print(response.type())
