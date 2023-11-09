from roles.BaseRole import Role
from utils.constants import INSTRUCTIONS_BY_ROLE

# 총감독 클래스
class Director(Role):
  def __init__(self, requestId):
    super().__init__("총감독", requestId)
    self.workers = [role for role in INSTRUCTIONS_BY_ROLE.keys() if role != "총감독"]
  
  # 컷 씬 개수 조회 메서드
  def get_total_scenes(self, message):
    return len([message for message in message.split("\n") if message.startswith("컷") and message.endswith(":")])

  def find_scene_index(self, messages, scene_number):
    for index, message in enumerate(messages):
      if f"컷 {scene_number}" in message:
        return index
    
    return -1

  # 메시지에서 역할과 내용을 추출하는 메서드
  def get_message_with_role(self, message):
    for role in self.workers:
      if role in message:
        return role, message.split(":")[1].strip()

  # 메시지 파싱 메서드
  def parse_scene(self, message, scene_number):
    messages, result = message.split("\n"), {}
    scene_index = self.find_scene_index(messages, scene_number)

    for index in range(scene_index + 1, len(messages)):
      parsed = self.get_message_with_role(messages[index])

      if parsed != None:
        result[parsed[0]] = parsed[1]

      if len(result.keys()) == len(self.workers):
        break

    return result