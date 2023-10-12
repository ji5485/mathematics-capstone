from roles.BaseRole import Role

# 촬영감독 클래스
class Cinematographer(Role):
  def __init__(self):
    super().__init__("촬영감독")

  def parse_scene(self, message):
    return message.split(":")[1]