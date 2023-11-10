from google.cloud import texttospeech

class TextToSpeech():

    #나레이션 text-to-speech 하는 메서드
    def text_to_speech(self,narration,scene_num):
        
        client = texttospeech.TextToSpeechClient()

        sentence = self.narration

        synthesis_input = texttospeech.SynthesisInput(text=sentence)

        voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
        )
        
        with open(f"컷{scene_num}", "wb") as out:
            out.write(response.audio_content)
