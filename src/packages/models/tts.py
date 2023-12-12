from gtts import gTTS

class TTS:
  def create(self, prompt, directory):
    tts = gTTS(text=prompt, lang="en")
    tts.save(directory + "/audio.mp3")
