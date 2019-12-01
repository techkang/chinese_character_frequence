# 中文汉字频率
## 简介
本仓库粗略实现了中文汉字频率统计，可以用于有简单需求的场景。
## 来源
语料来自[大规模中文自然语言处理语料 Large Scale Chinese Corpus for NLP](https://github.com/brightmart/nlp_chinese_corpus)中维基百科语料，统计代码如下：
```python
import os
import json
from collections import defaultdict

frequent = defaultdict(int)
dirs  = os.listdir('.')
for fold in dirs:
    if fold.startswith('A'):
        files = os.listdir(fold)
        for file in files:
            with open(os.path.join(fold,file),encoding='utf-8') as f:
                for line in f:
                    data = json.loads(line.strip())["text"]
                    for char in data:
                        frequent[char]+=1
info = [(v,k) for k,v in frequent.items()]
info.sort(reverse=True)
total = sum([v for v,k in info])
with open('frequence.txt','w',encoding='utf-8') as f:
    for v,k in info:
        f.write(f'{k}\t{v}\t{v/total}\n')
```

## 注意
- 统计结果可能不包含所有中文字符
- 统计结果包含非中文字符
- 统计结果不能反应所有可见中文字符的平均分布