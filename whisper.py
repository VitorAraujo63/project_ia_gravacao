#!pip install openai-whisper (https://www.youtube.com/watch?v=OEPkmsJmY2I)
# ffmpeg (https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)
#!pip install setuptools-rust

import whisper

model = whisper.load_model("base")
result = model.transcribe("Gravação.mp3")
print(result["text"])