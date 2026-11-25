# vLLM Bangla — Qwen2.5-7B-Instruct দিয়ে নিজের OpenAI-compatible LLM সার্ভার

vLLM দিয়ে GPU-তে দ্রুত LLM সার্ভার চালান।

- **Model:** https://huggingface.co/Qwen/Qwen2.5-7B-Instruct (Qwen2.5-7B-Instruct — বাংলা ভালো বোঝে)

## কী আছে / What is inside

- `serve-bangla.sh` — `vllm serve` কমান্ড: Qwen2.5-7B-Instruct মডেল OpenAI-compatible API হিসেবে চালায় `http://localhost:8000`-এ।
- `client-bangla.py` — শুধু Python stdlib (urllib) দিয়ে লেখা ক্লায়েন্ট: সার্ভারকে বাংলায় প্রশ্ন করে উত্তর ছাপে। কোনো extra প্যাকেজ লাগে না।

## যা ঠিক করা হয়েছে / What was fixed

- ডক্সে শুধু ইংরেজি উদাহরণ — এখানে বাংলা প্রশ্ন-উত্তরের রেডি উদাহরণ দেওয়া: সার্ভার চালু করে ক্লায়েন্ট চালালেই বাংলায় উত্তর আসে।
- মডেলের নাম আন্দাজে লেখা হয়নি — `Qwen/Qwen2.5-7B-Instruct` Hugging Face API দিয়ে যাচাই করা হয়েছে (text-generation, ৬৫ লাখ+ ডাউনলোড)।
- সার্ভার কমান্ডে `bash -n` যাচাই করা হয়েছে; ক্লায়েন্টে কোনো third-party প্যাকেজ নেই বলে `pip install` ছাড়াই চলে।

## Requirements / যা লাগবে

- **GPU আবশ্যক** — NVIDIA GPU, কমপক্ষে ১৬ GB VRAM (Qwen2.5-7B-Instruct চালাতে)। CPU-তে vLLM চলে না বললেই চলে।
- Python 3.10+ ও pip
- vLLM ইনস্টল:

```bash
pip install vllm
```

> ক্লায়েন্টের জন্য আলাদা কিছু ইনস্টল করতে হয় না — শুধু Python 3 stdlib ব্যবহার করা হয়েছে। `openai` প্যাকেজ দিয়ে করতে চাইলে `pip install openai` দিন, তারপর `OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")` ব্যবহার করুন।

## ব্যবহার / How to use

```bash
# 1. সার্ভার চালু করুন (প্রথমবার মডেল ডাউনলোড হবে, ~15 GB)
bash serve-bangla.sh

# 2. আরেকটা টার্মিনালে ক্লায়েন্ট চালান
python3 client-bangla.py
```

সার্ভার তৈরি হলে লগে `Application startup complete` দেখাবে। ক্লায়েন্ট প্রশ্ন করবে: "বাংলাদেশের জাতীয় মাছ কোনটি?" — উত্তর বাংলায় আসবে।

সার্ভার বন্ধ করতে সার্ভারের টার্মিনালে `Ctrl+C` চাপুন।
