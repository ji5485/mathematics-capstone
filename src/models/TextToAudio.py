#pip install git+https://github.com/huggingface/transformers.git
#!python3 -m pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft

from transformers import AutoProcessor, MusicgenForConditionalGeneration
from audiocraft.utils.notebook import display_audio
import scipy
import os
class TextToAudio():
     def text_to_audio(self, second, descriptions, scene_num):
        
        
        processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
        model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")


        output = processor(
            text=self.descriptions,
            padding=True,
            return_tensors="pt",
        )
        model.set_generation_params(duration=second)
        audio_values = model.generate(**output, max_new_tokens=256)
        OUTPUT_FILENAME = f"컷{scene_num}"

        sampling_rate = model.config.audio_encoder.sampling_rate
        display_audio(audio_values, sample_rate=32000)
        scipy.io.wavfile.write(os.getcwd(),f"{OUTPUT_FILENAME}.wav", rate=sampling_rate, data=audio_values[0, 0].numpy())
        