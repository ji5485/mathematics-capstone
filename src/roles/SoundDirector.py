from roles.BaseRole import Role

# 음향감독 클래스
class SoundDirector(Role):
  def __init__(self, requestId):
    super().__init__("음향감독", requestId)

  def parse_scene(self, messages):
    parsed = {}

    for message in messages.split("\n"):
      splitted = message.split(":")

      if len(splitted) != 2:
        continue
      
      parsed[splitted[0].strip()] = splitted[1].strip()

    return parsed