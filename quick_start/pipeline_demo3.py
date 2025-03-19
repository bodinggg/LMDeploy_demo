from lmdeploy import pipeline, GenerationConfig, TurbomindEngineConfig


if __name__ == '__main__':
    backend_config = TurbomindEngineConfig(tp=2)
    gen_config = GenerationConfig(top_p=0.8,
                                top_k=40,
                                temperature=0.8,
                                max_new_tokens=1024)

    pipe = pipeline('/home/featurize/work/LLaMA-Factory/Qwen/Qwen2.5-3B-Instruct')
    prompts = [[{
        'role': 'user',
        'content': '你好，介绍下你自己'
    }], [{
        'role': 'user',
        'content': '上海是'
    }]]
    response = pipe(prompts,
                    gen_config=gen_config)
    print(response)
