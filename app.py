from flask import Flask, render_template, request, jsonify
import os
import re
import subprocess
from pytubefix import YouTube
from pathlib import Path
import shutil  # Para detectar o FFmpeg no sistema

app = Flask(__name__)

# Obtém o diretório de Downloads do usuário
DOWNLOAD_DIR = str(Path.home() / "Downloads")

# Detectar o caminho do FFmpeg automaticamente
FFMPEG_PATH = shutil.which("ffmpeg")

if not FFMPEG_PATH:
    raise FileNotFoundError("Erro: FFmpeg não encontrado no sistema. Certifique-se de que ele está instalado e acessível no PATH.")

# Função para sanitizar o nome do arquivo
def sanitize_filename(name):
    name = re.sub(r'[\/:*?"<>|]', '_', name)  # Remove caracteres inválidos
    name = name.replace(" ", "_")  # Substitui espaços por "_"
    return name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form.get('url')
    
    if not video_url:
        return jsonify({"error": "Erro: Nenhuma URL fornecida!"}), 400

    try:
        yt = YouTube(video_url)
        video_title = sanitize_filename(yt.title)
        
        final_output = os.path.join(DOWNLOAD_DIR, f"{video_title}.mp4")

        # Verifica se o arquivo já existe para evitar múltiplos downloads repetidos
        if os.path.exists(final_output):
            return jsonify({"success": "O vídeo já foi baixado e está salvo em Downloads."})

        video_stream = yt.streams.filter(adaptive=True, mime_type="video/mp4").order_by("resolution").desc().first()
        audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4").order_by("abr").desc().first()
        
        if not video_stream or not audio_stream:
            return jsonify({"error": "Erro: Não foi possível encontrar streams de vídeo e áudio compatíveis."}), 500

        video_path = os.path.join(DOWNLOAD_DIR, f"{video_title}_video.mp4")
        audio_path = os.path.join(DOWNLOAD_DIR, f"{video_title}_audio.mp4")

        video_stream.download(output_path=DOWNLOAD_DIR, filename=f"{video_title}_video.mp4")
        audio_stream.download(output_path=DOWNLOAD_DIR, filename=f"{video_title}_audio.mp4")

        subprocess.run([
            FFMPEG_PATH, "-i", video_path, "-i", audio_path,
            "-c:v", "copy", "-c:a", "aac", final_output, "-y"
        ], check=True)

        os.remove(video_path)
        os.remove(audio_path)

        return jsonify({"success": "Download concluído! O arquivo foi salvo em Downloads."})
    
    except Exception as e:
        return jsonify({"error": f"Erro: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
