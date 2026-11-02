<div align="center">

# 🗣️ OuteTTS API

**A FastAPI text-to-speech service for English, Chinese, Japanese and Korean, powered by OuteTTS.**

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"> <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=white" alt="Hugging Face"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">

</div>

## 📌 Overview

Wraps the open-source **OuteTTS-0.2-500M** speech model in a small FastAPI service. You send text and a language, and the API returns synthesised speech using a language-specific speaker preset. A simple HTML page is included for trying it from the browser.

## ✨ Features

- `GET /languages/{language}?inputtext=...`: synthesise speech in English, Chinese, Japanese or Korean
- Per-language speaker "tunes" (`tunes.py`)
- CORS enabled for a browser front end (`index.html`)

## 🚀 Getting Started

```bash
git clone https://github.com/KamranUmer/OuteTTS.git
cd OuteTTS
pip install fastapi uvicorn outetts
uvicorn app:app --reload
# open http://127.0.0.1:8000/docs to try the endpoints
```

## 📁 Project Structure

```
OuteTTS/
├── app.py             # FastAPI routes
├── model_config.py    # OuteTTS model setup
├── languages.py       # supported languages
├── tunes.py           # speaker presets per language
├── index.html         # browser demo
└── main.py / test.py  # local experiments
```

## 🙏 Acknowledgements

- [OuteTTS](https://github.com/edwko/OuteTTS) by OuteAI

---

<div align="center">

Built by <a href="https://github.com/KamranUmer"><b>Kamran Umer</b></a> · ⭐ Star the repo if you find it useful

</div>
