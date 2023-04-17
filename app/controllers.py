import os
import pyocr
import pyocr.builders
import openai
from PIL import Image

# 文字認識機能
def ocr_image(image_path):
    tool = pyocr.get_available_tools()[0]
    lang = 'jpn'  # 日本語を指定
    image = Image.open(image_path)
    text = tool.image_to_string(
        image,
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    return text


# OpenAIAPIによる要約と修正
def process_gpt(text, action):
    openai.api_key = os.environ["OPENAI_API_KEY"]

    if action == "summarize":
        prompt = f"以下のテキストを要約してください:\n\n{text}\n\n要約:"
    elif action == "correct":
        prompt = f"以下のテキストの誤字脱字を修正してください:\n\n{text}\n\n修正後のテキスト:"
    else:
        raise ValueError("Invalid action")

    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=800,  
        n=1,
        stop=None,
        temperature=0.5,
    )

    processed_text = response.choices[0].text.strip()
    return processed_text