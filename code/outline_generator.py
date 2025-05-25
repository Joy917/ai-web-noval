import os
from datetime import datetime
import asyncio
import httpx
import json
import yaml
import logging

# 获取当前脚本所在目录，拼接config路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "../config/settings.yaml")

# 读取配置
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

OUTPUT_DIR = config["output_path"]["outlines"]
LOG_LEVEL = getattr(logging, config.get("log", {}).get("level", "INFO").upper())
base_log_file = config.get("log", {}).get("file", "ai_novel.log")

# 日志文件名加上启动时间戳，避免覆盖
start_time = datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir, log_filename = os.path.split(base_log_file)
log_name, log_ext = os.path.splitext(log_filename)
log_file_with_time = os.path.join(
    log_dir, f"{log_name}_{start_time}{log_ext}"
)

# 日志初始化
logger = logging.getLogger("ai_novel")
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# 控制台
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
# 文件
file_handler = logging.FileHandler(log_file_with_time, encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = config["model_parameters"]["model_name"]
MAX_TOKENS = config["model_parameters"]["max_tokens"]
TEMPERATURE = config["model_parameters"]["temperature"]

# 读取基础大纲prompt
PROMPT_PATH = os.path.join(BASE_DIR, "../config/prompts/outline_prompt.txt")
with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    BASE_OUTLINE_PROMPT = f.read()

async def generate_outline_with_ollama(extra_prompt, model=MODEL, max_tokens=MAX_TOKENS, temperature=TEMPERATURE):
    # 拼接基础prompt和本次补充说明
    prompt = f"{BASE_OUTLINE_PROMPT}\n\n补充说明：\n{extra_prompt}\n"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,
        "options": {
            "temperature": temperature,
            "max_tokens": max_tokens
        }
    }
    async with httpx.AsyncClient(timeout=None) as client:
        logger.info("开始生成...")
        resp = await client.post(OLLAMA_API_URL, json=payload, timeout=None)
        outline_content = ""
        received_tokens = 0
        total_tokens = max_tokens
        last_percent = 0
        async for line in resp.aiter_lines():
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                token = data.get("response", "")
                outline_content += token
                received_tokens += 1
                percent = int(received_tokens / total_tokens * 100)
                if percent // 5 > last_percent // 5:
                    logger.info(f"生成中...【{percent}%】")
                    last_percent = percent
                if data.get("done"):
                    break
            except Exception:
                continue
        logger.info("生成完毕！")
        return outline_content

async def write_outline_async(stage, prompt, file_path):
    outline_content = await generate_outline_with_ollama(prompt)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# Outline: {stage}\n\n{outline_content}")
    logger.info(f"文件位置为：{file_path}")
    return outline_content

async def main():
    while True:
        stage = input("请输入大纲阶段名（如stage1、stage2等）：")
        prompt = input("请输入本阶段大纲生成提示词（prompt）：")
        current_time = datetime.now().strftime("%Y.%m.%d-%H.%M")
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        filename = f"[Outline] {stage} - {current_time}.txt"
        file_path = os.path.join(OUTPUT_DIR, filename)
        outline_content = await write_outline_async(stage, prompt, file_path)

        while True:
            modify = input("是否有修改点需要补充？(y/n)：")
            if modify.lower() == "y":
                modify_point = input("请输入修改点：")
                # 组合原大纲和修改点，重新生成
                new_prompt = (
                    f"以下是已生成的大纲：\n{outline_content}\n\n"
                    f"请根据以下修改点对大纲进行调整和完善：\n{modify_point}\n"
                    "请输出修改后的完整大纲。"
                )
                outline_content = await write_outline_async(stage, new_prompt, file_path)
            else:
                break

        cont = input("继续生成下一个阶段大纲？(y/n)：")
        if cont.lower() != "y":
            break

if __name__ == "__main__":
    asyncio.run(main())