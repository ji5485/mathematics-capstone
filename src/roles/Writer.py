from roles.BaseRole import Role

# 작가 클래스
class Writer(Role):
  def __init__(self):
    super().__init__("작가")

  def parse_scene(self, message):
    return message.split(":")[1]