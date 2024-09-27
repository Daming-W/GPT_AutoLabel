from openai import OpenAI


import json
import argparse

# Function to read API key from a text file
def load_api_key(txt):
    with open(txt, 'r') as file:
        api_key = file.read().strip()  # Read and strip any whitespace
    return api_key

def replace_newlines_in_json_string(s):
    return s.replace('\n', ' ')

def label_single(args, prompt_dict, txt):

    # Combine prompt
    prompt = prompt_dict["task"] + prompt_dict["samples"] + "Now please analyze and set a label for: " + txt
    print(prompt)

    # Make conversation with OpenAI API using the correct method for chat-based models
    hat_completion = client.completions.create(model="gpt-4",  # Ensure you're using the correct model
    prompt=[
        {"role": "system", "content": prompt_dict["role"]},
        {"role": "user", "content": prompt},
    ],
    temperature=0.9,
    top_p=0.7,
    max_tokens=2000)

    # Process and print the result
    result = hat_completion.choices[0].message.content
    result = json.loads(replace_newlines_in_json_string(result))

    print(result)

if __name__ == "__main__":
    print("start testing")

    # Argument parser to get command line arguments
    parser = argparse.ArgumentParser(description="Process data.")
    parser.add_argument('--input_dir', type=str, default='./data', 
                        help='Path to the annotations files directory.')
    parser.add_argument('--output_dir', type=str, default='./data', 
                        help='Path to the annotations files directory.')
    parser.add_argument('--n_process', type=int, default=8, 
                        help='Number of processes to use.')
    parser.add_argument('--api_key', type=str, default="api_key.txt",
                        help='API key for OpenAI.')
    args = parser.parse_args()

    # Load the API key from the specified file
    api_key = load_api_key(args.api_key)
    client = OpenAI(api_key=api_key)
      # Set the API key for OpenAI

    # Define prompt dictionary
    prompt_dict = {
        "role": " You are an advanced data analyst with extensive knowledge of finance and a deep understanding of market dynamics. \
                    You are able to analyze news content and assess its potential impact on the market.",
        "task": " Based on the provided news content, analyze the overall tone and content of the news and determine its sentiment toward the market. \
                    Your task is to assign a label to the news based on its text: \
                    0 indicates the news has a negative impact on the market. \
                    1 indicates the news is neutral or positive for the market. \
                    -1 indicates the news is ambiguous or unclear, and its impact on the market cannot be determined.",
        "samples": "Here are a few samples for you to understand and imitate: \
                    [CLS]每经AI快讯，3月22日，上海钢联(300226)发布数据显示，今日电池级碳酸锂价格较上次持平，均价报11.35万元/吨。[SEP], Label : 0 \
                    [CLS]（原标题：“天价锂矿”二度拍卖：首轮5人报名，22分钟达到4亿封顶价）证券时报网讯，25日早间，四川雅江斯诺威矿业54.2857%股权拍卖10时正式开始，“天价锂矿”争夺战再度拉开帷幕。[SEP], Label : 1."
    }

    # Call the function to label the input text
    label_single(args, prompt_dict, '明日大涨！')
