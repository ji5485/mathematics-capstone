from gtts import gTTS
from .base_model import Model

class TTS(Model):
  def create(self, prompt, directory):
    result = gTTS(text=prompt, lang="en")
    result.save(directory + "/narration.mp3")
