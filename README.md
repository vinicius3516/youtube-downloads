# Flask YouTube Downloader

Este projeto permite baixar vídeos do YouTube com uma interface interativa usando Flask.

## 📌 Como Instalar e Rodar

### 1️⃣ Clone o repositório
```sh
git clone https://github.com/seu-usuario/flask-youtube-downloader.git
cd flask-youtube-downloader
```

### 2️⃣ Crie um ambiente virtual e instale as dependências
```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Baixe o FFmpeg e coloque na pasta `bin/`
Baixe o **FFmpeg** [aqui](https://ffmpeg.org/download.html), extraia e coloque na pasta `bin/`.

### 4️⃣ Rode a aplicação Flask
```sh
python app.py
```

Agora, acesse [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador. 🚀

## 📂 Estrutura do Projeto
```
Flask_Youtube_Downloader/
│── bin/                    # FFmpeg deve estar aqui
│── templates/               # HTML
│   ├── index.html           # Página principal
│── static/                  # CSS e JS
│   ├── styles.css           # Estilos
│── app.py                   # Código Flask
│── requirements.txt         # Dependências
│── README.md                # Instruções do projeto
```

## 🛠 Tecnologias Usadas
- Python + Flask
- pytubefix
- FFmpeg
- HTML + CSS (Bootstrap-like)

📢 **Agora, você pode baixar vídeos do YouTube facilmente!** 🚀
