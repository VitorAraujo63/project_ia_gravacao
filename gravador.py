#!pip install pyaudio wave (https://www.youtube.com/watch?v=b1ErnwAsJx4)
# baixar cuda pytorch
# baixar 

import pyaudio
import wave
import whisper
from pathlib import Path
import os.path

while True:
    nome_arquivo = input("Digite o nome do arquivo: ")
    if os.path.isfile(nome_arquivo+'.mp3') == True:
        print('O nome do arquivo ja existe...')
        continue
    else:
        print("Nome escolhido com sucesso!")
        break


audio = pyaudio.PyAudio()

stream = audio.open(
    input=True,
    format=pyaudio.paInt16,
    channels=1,
    rate=44000,
    frames_per_buffer=1024,
)

frames = []


try:
    while True:
        bloco = stream.read(1024)
        frames.append(bloco)
except KeyboardInterrupt:
    pass

stream.start_stream()
stream.close()
audio.terminate()
arquivo_final = wave.open(nome_arquivo+'.mp3', "wb")
arquivo_final.setnchannels(1)
arquivo_final.setframerate(44000)
arquivo_final.setsampwidth(audio.get_sample_size(pyaudio.paInt16))

arquivo_final.writeframes(b"".join(frames))

arquivo_final.close()

while True:
    escolha = input("Você deseja salvar essa reuniao ? (s/n): ")

    if escolha == 's':
        model = whisper.load_model("small")
        result = model.transcribe(nome_arquivo+'.mp3')

        with open(nome_arquivo+'.txt', "+a") as arquivo:
            arquivo.write(result['text'])
        print("Reunião salva em um arquivo de texto!")
        break
    else:
        escolha2 = input("Você tem certeza que deseja excluir a reuniao ? (s/n): ")

        if escolha2 == 's':
            Path(nome_arquivo+'.mp3').unlink()
            print("Excluindo os arquivos...")
            break
        else:
            pass