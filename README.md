# 武汉大学数据新闻实验2
## 实验内容
使用GPT-2模型、LLM模型根据新闻标题生成新闻内容，并与原文进行比较分析，分析模型可能存在的问题。

## 实验环境
- python
- transformers
- torch
- tqdm
- zhipuai
- intel_extension_for_pytorch (optional)

详见conda_requirements.txt和pip_requirements.txt。请先使用conda创建环境并安装conda_requirements.txt中的包，再使用pip安装pip_requirements.txt中的包。

## 使用指南
请先将新闻写入sample/news.txt，标题和内容各占一行（可参考sample/news_example.txt的格式），然后通过环境变量配置智谱AI的API_KEY（如果没有，请前往[智谱AI](https://open.bigmodel.cn)注册并获取API_KEY），
```shell
export API_KEY=your_api_key
```
最后运行`python -u main.py`即可。输出将被输出到sample/result.txt。输出的内容与格式可以参考sample/result_example.txt。