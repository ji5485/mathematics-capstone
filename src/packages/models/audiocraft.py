import scipy
from audiocraft.models import musicgen
from .base_model import Model

class Audiocraft(Model):
  def __init__(self):
    self.model = musicgen.MusicGen.get_pretrained('facebook/musicgen-small')
    self.model.generation_params = { 'use_sampling': True, 'temp': 1.0, 'top_k': 250, 'top_p': 0 }
    self.model.set_generation_params(duration=10)

  def create(self, prompt, directory):
    result = self.model.generate([prompt], progress=True)
    scipy.io.wavfile.write(f"{directory}/bgm.wav", self.model.sample_rate, result[0, 0].numpy())
