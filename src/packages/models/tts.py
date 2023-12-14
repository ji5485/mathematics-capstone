from gtts import gTTS
from .base_model import Model

class TTS(Model):
  def create(self, prompt, directory):
    tts = gTTS(text=prompt, lang="en")
    tts.save(directory + "/narration.mp3")
