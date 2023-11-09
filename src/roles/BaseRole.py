import openai
from utils.constants import INSTRUCTIONS_BY_ROLE

class Role:
  def __init__(self, role, requestId):
    self.role = role
    self.requestId = requestId
    self.system_instruction = INSTRUCTIONS_BY_ROLE[role].get('system', "")
    self.assistant_instruction = INSTRUCTIONS_BY_ROLE[role].get('assistant', "")

  # GPT-3.5와 상호작용하는 함수
  def interact(self, message, print_result=True):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        { "role": "system", "content": self.system_instruction },
        { "role": "assistant", "content": self.assistant_instruction },
        { "role": "user", "content": message }
      ],
      stream=True
    )

    if print_result:
      print(f" {self.role} ".center(100, "=") + "\n\n")

    result = ""

    for chunk in response:
      current_chat = chunk.choices[0].get('delta', {}).get('content')
      
      if current_chat:
        if print_result:
          print(current_chat, end="")
        result += current_chat   
    
    if print_result:
      print("\n\n" + "=" * 100 + "\n\n")

    return result

