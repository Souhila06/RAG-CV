# RAG-CV

Ce projet propose une interface web permettant d'uploader des CVs en tant qu'inspiration pour le LLM. Par la suite un prompt est disponible pour modifier le CV.
La sortie est un texte. 


## Prérequis

Version de python conseillée : 3.11.0

```bash
wget https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q8_0.gguf -O LLM/qwen2.5-1.5b-instruct-q8_0.gguf

pip install -r requirements.txt

export CMAKE_ARGS="-DGGML_CUDA=on"
pip install llama-cpp-python
```

## Usage

```bash
streamlit run web_app.py
```
