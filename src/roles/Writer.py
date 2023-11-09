from roles.BaseRole import Role

# 작가 클래스
class Writer(Role):
  def __init__(self, requestId):
    super().__init__("작가", requestId)

  def parse_scene(self, message):
    return message.split(":")[1]