xcode-select --install
pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
pip3 install --upgrade pip
CMAKE_ARGS="-DLLAMA_METAL=on" pip3 install llama-cpp-python --upgrade
pip3 install --no-cache-dir -r requirements.txt