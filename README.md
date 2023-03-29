# auto-writer-code

### General
This code aims to write code like an AI.

### Pre-requisites

- [ffmeg](https://ffmpeg.org/download.html)

- Delete identation, autocompletion in VSCode or use `vscode-app`.

- Python 3.8

- ```bash
  pip install -r requirements.txt
  ```

### Usage

> Once the command is launched, you have 3 seconds to get to where the code should be written.

Using defaults : 
```bash
python main.py
```

With recording: 
```bash
python main.py -r
```
Update video properties in `config.json`.

Run vscode-app:
```bash
cd vscode-app
npm i
npm run dev
```

