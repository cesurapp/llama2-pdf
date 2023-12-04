# Llama2 Flask AI Server using LLamaCPP

__Supported:__
- CPU
- M1 Metal GPU 
- Cuda GPU

__Warning:__
* Docker MacOS üzerinde en az 5 kat yavaş çalışıyor, sanallaştırmadan kaynaklı. Native kurulum yapın.
* Linux üzerinde GPU kullanımı için ekran kartı sürücüleri host sisteme yüklenmeli ve docker kullanılacak ise "Cuda Container Toolkit" yüklenmeli
* Model dosyaları HuggingFace'ten otomatik olarak "models" dizinine indirilir. Bu dizin eğer docker ile kullanılacak ise paylaşım yapılmalı.
* MacOS için `xcode-select --install` gereklidir.
* __7b__ 16GB - __13b__ 32GB - __70b__ 140GB ortalama Ram|vRam gerektirir.
* __70b__ CPU üzerinde çalıştırılmamalıdır.

__Dependencies/Model:__
* [LLaMA.cpp](https://github.com/ggerganov/llama.cpp)
* [LLaMA.cpp Python Binding](https://github.com/abetlen/llama-cpp-python)
* [Nvidia Cuda Pytorch Container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch)
* [Llama2 Chat Prompt Template](https://gpus.llm-utils.org/llama-2-prompt-template/)
* [Llama2 7B Chat GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)
* [Llama2 7B Chat GGUF Uncensored](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF)
* [Llama2 13B Chat GGUF](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF)
* [Llama2 70B Chat GGUF](https://huggingface.co/TheBloke/Llama-2-70B-Chat-GGUF)

__ENV:__ 

The predefined models are in the `src/models.py` file.
```env
MODEL=7b-Q4KM-CHAT
HOST=0.0.0.0
PORT=3000
```

## Installation

### Mac M1/M2 Metal GPU
```bash
git clone <repo>
sh ./install_mac.sh
```

### Linux for CPU
```bash
git clone <repo>
sh ./install_linux.sh
```

### Linux for GPU
* Install [Cuda Driver](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html)

```bash
git clone <repo>
sh ./install_linux.sh
```

### Docker (Only Linux, very slow on MacOS)
* Install [Cuda Driver](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html)
* Install [Cuda Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
```
docker compose up --remove-orphans --build
```

## Run 
```bash
python3 src/server.py
```

## API

HTTP Server: 127.0.0.1:3000
```
endpoint: http://127.0.0.1:3000/ask

RAW JSON Content:

{
    "textContext": "My name is Ramazan Apaydın",
    "pdfContextBase64": "",
    "prompts": [
        "What is person's full name?",
        "What is person's role?",
        "What are their skills?"
    ]
}
```