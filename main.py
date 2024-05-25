import generation
import os
from zhipuai import ZhipuAI

input_path='sample/news.txt'
output_path='sample/result.txt'
api_key=os.getenv('API_KEY')

def main():
    if not os.path.exists(output_path):
        os.makedirs(os.path.dirname(output_path),exist_ok=True)
    open(output_path, 'w').close()
    with open(input_path,'r') as f:
        news = f.readlines()

    for i in range(len(news)//2):
        title = news[i*2].strip()
        with open(output_path,'a') as f:
            f.write('新闻'+str(i+1)+':\n')
            f.write('1. 新闻原文：\n')
            f.write(news[i*2])
            f.write(news[i*2+1])
            f.write('\n')

        gpt2=generation.main(title)

        client = ZhipuAI(api_key=api_key) # 填写您自己的APIKey
        response = client.chat.completions.create(
            model="glm-3-turbo",  # 填写需要调用的模型名称
            messages=[
                {"role": "user", "content": "作为一名专业记者，帮助我撰写一篇新闻稿，请使用纯文本格式输出，并不要输出额外的提示信息"},
	            {"role": "assistant", "content": "当然，为了创作一篇吸引人的新闻稿，请告诉我一些关于新闻的信息"},
                {"role": "user", "content": title}
            ],
        )
        glm3=response.choices[0].message.content.replace('\n','')
        
        user_message="这是新闻原文："+news[i*2+1]+"这是大模型GPT-2生成的新闻："+gpt2+"\n作为一名专业的AI工程师，比较它们，分析大模型GPT-2可能存在的问题，以及出现这些问题的可能原因。以纯文本格式输出。"
        response = client.chat.completions.create(
            model="glm-3-turbo",  # 填写需要调用的模型名称
            messages=[
                {"role": "user", "content": user_message}
            ],
        )
        comparison=response.choices[0].message.content.replace('\n\n','\n')
                
        with open(output_path,'a') as f:
            f.write('2. GPT-2生成新闻：\n')
            f.write(gpt2)
            f.write('\n\n')
            f.write('3. 大模型生成新闻：\n')
            f.write(glm3)
            f.write('\n\n')
            f.write('4. 对比分析：\n')
            f.write(comparison)
            f.write('\n\n')

if __name__ == '__main__':
    main()