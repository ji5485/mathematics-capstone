from roles.BaseRole import Role
from models.hotshot import Hotshot

# 촬영감독 클래스
class Cinematographer(Role):
  def __init__(self, requestId):
    super().__init__("촬영감독", requestId)
    self.model = Hotshot(requestId)
    self.files = []

  # 메시지 파싱 메서드
  def parse_scene(self, message):
    return message.split(":")[1]

  # GIF 생성 메서드
  def create(self, command):
    file_name = self.model.generate(command)
    self.files.append(file_name)
    return file_name