import os
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip, CompositeAudioClip, concatenate_videoclips

class Creator:
  def __init__(self, request_id):
    self.request_id = request_id
    self.clips = []

  def create_scene_clip(self, scene_number):
    directory = os.path.join(os.getcwd(), "src", "artifacts", self.request_id, f"scene-{scene_number}")

    if not os.path.exists(directory):
      raise Exception("Directory not found!")
    
    narration_file = os.path.join(directory, "narration.mp3")
    bgm_file = os.path.join(directory, "bgm.mp3")
    image_file = os.path.join(directory, "image.png")

    narration_clip = AudioFileClip(narration_file)
    background_music_clip = AudioFileClip(bgm_file).volumex(0.1)
    composite_audio_clip = CompositeAudioClip([narration_clip, background_music_clip]).volumex(0.5)
    duration = narration_clip.duration + 3

    image_clip = ImageClip(image_file, duration=duration).crossfadein(0.5).set_audio(composite_audio_clip)

    final_audio = CompositeVideoClip([image_clip])
    final_clip = final_audio.set_duration(duration).set_fps(24).fadeout(0.5)

    self.clips.append(final_clip)

  def create_advertisement(self):
    if not os.path.exists(os.path.join(os.getcwd(), "src", "result")):
      os.makedirs(os.path.join(os.getcwd(), "src", "result"))

    video_path = os.path.join(os.getcwd(), "src", "result", f"{self.request_id}.mp4")
    final_clip = concatenate_videoclips(self.clips, method="compose")
    final_clip.write_videofile(video_path, fps=24)
