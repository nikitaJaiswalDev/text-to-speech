from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

class TextToSpeech():
    def __init__():
        preload_models()
        return {"Greet": "Hello"}
    
    def predict(self, text: str):
        audio_array = generate_audio(text)
        result = Audio(audio_array, rate=SAMPLE_RATE)
        return result