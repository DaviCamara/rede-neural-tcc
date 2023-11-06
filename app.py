import os
from flask import Flask, request
from MLExport import avaliar_modelo
import wave 
import numpy as np 
from pydub import AudioSegment
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/', methods=['POST'])
def upload_audio():
    print("entrei")
    if 'audio' not in request.files:
        return "No file part", 400

    audio_file = request.files['audio'] 

    if audio_file.filename == '':
        return "No selected file", 400

    if audio_file:
        
        ogg_path = 'uploaded_audio.ogg'
        audio_file.save(ogg_path)

        # Converter o arquivo OGG para WAV
        audio_data = AudioSegment.from_file(ogg_path, format="ogg")
        wav_path = 'aaaaaaa.wav'
        audio_data.export(wav_path, format="wav")

        
        # Agora você pode passar o arquivo WAV para a função criar_dataframe()
        avaliar_modelo(wav_path)

        
        return avaliar_modelo(wav_path)
    #"Audio file received and converted to WAV successfully", 200
        

if __name__ == "__main__":
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '5000')
    app.run(host=host, port=int(port), debug=True)
