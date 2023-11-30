from fastapi import FastAPI
from models import TextToSpeech

app = FastAPI()

@app.get('/')
async def root():
    tts = TextToSpeech()
    text_to_convert = "Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe."
    audio_output = tts.predict(text_to_convert)

    print('---audio_output--', audio_output)
    return {'example': 'This is an example'}