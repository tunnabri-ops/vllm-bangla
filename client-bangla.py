#!/usr/bin/env python3
"""vLLM Bangla ক্লায়েন্ট — শুধু Python stdlib (urllib) দিয়ে।

সার্ভার আগে চালু করুন (serve-bangla.sh), তারপর এই ফাইল চালান:
    python3 client-bangla.py

কোনো third-party প্যাকেজ লাগে না। openai প্যাকেজ দিয়ে করতে চাইলে:
    pip install openai
    OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
"""

import json
import sys
import urllib.error
import urllib.request

BASE_URL = "http://localhost:8000/v1"
MODEL = "Qwen/Qwen2.5-7B-Instruct"

QUESTION = "বাংলাদেশের জাতীয় মাছ কোনটি এবং কেন এটি জাতীয় মাছ হিসেবে বেছে নেওয়া হয়েছে? সংক্ষেপে বাংলায় উত্তর দাও।"


def chat(question: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "তুমি একজন সহায়ক বাংলা সহকারী। সবসময় বাংলায়, সংক্ষেপে ও সঠিকভাবে উত্তর দাও।",
            },
            {"role": "user", "content": question},
        ],
        "temperature": 0.7,
        "max_tokens": 512,
    }
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"].strip()


def main() -> int:
    print(f"প্রশ্ন: {QUESTION}\n")
    try:
        answer = chat(QUESTION)
    except urllib.error.URLError as exc:
        print(
            "সার্ভারের সাথে সংযোগ হচ্ছে না। প্রথমে serve-bangla.sh চালিয়ে "
            f"সার্ভার চালু করুন (http://localhost:8000)।\nত্রুটি: {exc}",
            file=sys.stderr,
        )
        return 1
    except (KeyError, IndexError, ValueError) as exc:
        print(f"সার্ভারের উত্তর বোঝা যায়নি: {exc}", file=sys.stderr)
        return 1
    print(f"উত্তর:\n{answer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
