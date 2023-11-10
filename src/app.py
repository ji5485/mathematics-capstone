from utils.initialize import initialize
from roles.Director import Director
from roles.Writer import Writer
from roles.SoundDirector import SoundDirector
from roles.Cinematographer import Cinematographer
from models.TextToSpeech import TextToSpeech
import os 

initialize()

director = Director()
writer = Writer()
sound_director = SoundDirector()
cinematographer = Cinematographer()

def main():
  director_chat = director.interact("광고의 주제는 '행복'입니다.")
  total_scene = director.get_total_scenes(director_chat)

  current_path = os.getcwd()

  for scene_number in range(1, total_scene + 1):
    print(f"씬 {scene_number} 시작".center(100, "-") + "\n\n")
    description_by_scene = director.parse_scene(director_chat, scene_number)
    current_dir = os.makedirs(current_path+"/"+f"{director_chat}"+"/"+f"씬{scene_number}",exist_OK=True)
    os.chdir(current_dir)

    writer_chat = writer.interact(description_by_scene.get("작가"))
    narration = writer.parse_scene(writer_chat)

    TextToSpeech.text_to_speech(narration,scene_number)
    
    sound_director_chat = sound_director.interact(f"""
      총감독: {description_by_scene.get('음향감독')}
      나래이션: {narration}
    """)
    # 음향감독이 컷별로 제시한 초만큼 second에 넣어야 함(여기선 약 5초라고 가정)
    TextToAudio.text_to_audio(scene_number, 5, sound_director.parse_scene(sound_director_chat))

    cinematographer_chat = cinematographer.interact(f"""
      총감독: {description_by_scene.get('촬영감독')}
      음향: {sound_director.parse_scene(sound_director_chat).get('컨셉')}
      나래이션: {narration}
    """)

    print(f"""
      씬 {scene_number} 시나리오
      나래이션: {narration}
      음향 : {sound_director.parse_scene(sound_director_chat).get('컨셉')}
      촬영 : {cinematographer.parse_scene(cinematographer_chat)}
    """)

    print(f"씬 {scene_number} 종료".center(100, "-") + "\n\n")


main()
