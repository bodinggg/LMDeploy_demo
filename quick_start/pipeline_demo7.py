# 释放pipeline
from lmdeploy import pipeline

# with和.close()两种方法释放
with pipeline('internlm/internlm2_5-7b-chat') as pipe:
    response = pipe(['你好，介绍你自己', '上海是个啥'])
    print(response)
