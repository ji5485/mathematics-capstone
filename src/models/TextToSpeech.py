# pip install gtts

from gtts import gTTS
from utils.utils import createSceneDirectory

class TextToSpeech():

    # 나레이션 text-to-speech 파일 생성하는 메서드
    def generate(narration):

        file_name = 'TTS.mp3'

        tts = gTTS(
            text = narration,
            lang = 'ko'
        )

        createSceneDirectory():
        os.makedirs(f"{os.getcwd()}/TextToSpeech",exist_OK=True)
        os.chdir('TextToSpeech')
        tts.save(file_name)

