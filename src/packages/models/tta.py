!nvidia-smi
!python3 -m pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft

from audiocraft.models import musicgen
from audiocraft.utils.notebook import display_audio

class TTA:
    def __init__(self):
        # 모델 초기화
        self.model = musicgen.MusicGen.get_pretrained('facebook/musicgen-small', device='cuda')
        self.model.generation_params = {'use_sampling': True,
                                        'temp': 1.0,
                                        'top_k': 250,
                                        'top_p': 0}
        self.model.set_generation_params(duration=5)

    # 스크립트를 받아 음악을 생성하는 메서드
    def create(self, script):
        self.script = script
        tta = self.model.generate([script], progress=True)

        return tta
