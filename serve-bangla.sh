#!/usr/bin/env bash
# vLLM Bangla — Qwen2.5-7B-Instruct সার্ভার
# মডেল: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
# ডক্স: https://docs.vllm.ai/en/latest/getting_started/quickstart.html
# সার্ভার চালু হলে OpenAI-compatible API পাওয়া যায় http://localhost:8000/v1-এ।
set -euo pipefail

MODEL="Qwen/Qwen2.5-7B-Instruct"
HOST="0.0.0.0"
PORT="8000"

# vLLM ইনস্টল আছে কি না দেখুন
if ! command -v vllm >/dev/null 2>&1; then
    echo "vLLM পাওয়া যায়নি। প্রথমে ইনস্টল করুন:"
    echo "  pip install vllm"
    exit 1
fi

# GPU আছে কি না দেখুন (থাকলে তথ্য দেখান, না থাকলে সতর্ক করুন)
if command -v nvidia-smi >/dev/null 2>&1; then
    nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
else
    echo "সতর্কতা: nvidia-smi পাওয়া যায়নি — vLLM-এর জন্য NVIDIA GPU দরকার।"
    echo "GPU ছাড়া সার্ভার চালু নাও হতে পারে বা খুব ধীর হবে।"
fi

echo "মডেল চালু হচ্ছে: $MODEL"
echo "API ঠিকানা: http://localhost:$PORT/v1"
echo "বন্ধ করতে Ctrl+C চাপুন।"
echo

# --max-model-len 8192: একসাথে ৮ হাজার টোকেন পর্যন্ত কনটেক্সট
# --gpu-memory-utilization 0.9: GPU মেমরির ৯০% পর্যন্ত ব্যবহার
exec vllm serve "$MODEL" \
    --host "$HOST" \
    --port "$PORT" \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.9
