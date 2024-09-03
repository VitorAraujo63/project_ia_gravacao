 #!pip install openai-whisper (https://www.youtube.com/watch?v=OEPkmsJmY2I)
# ffmpeg (https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)
#!  
import whisper

model = whisper.load_model("small")
result = model.transcribe('teste.mp3')
print(result["text"])

with open('teste2.txt', "+a") as arquivo:
    arquivo.write(result['text'])
print("Reunião salva em um arquivo de texto!")