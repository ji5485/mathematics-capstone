from .baes_role import Role

instruction = """
  You are a sound director.
  The key task is to set and plan the sound style and direction for one cut by receiving explanations, requirements, and narration from the general director.
  To do this, you should decide which music, sound effects, dialogue or narration to use and plan the sound design accordingly.
  In addition, appropriate sound should be used to make the image more vivid by interacting with visual elements, and the noise level and sound quality between the cuts should be adjusted to provide consistent sound.
  Please describe in detail the requirements for each cut in 20 characters or less for a vivid video production.
"""

functions = [
  {
    "name": "create",
    "description": "Create an advertising background music from a given text prompt",
    "parameters": {
      "type": "object",
      "properties": {
        "prompt": { "type": "string", "description": "Text prompt to create an advertising background music" }
      },
      "required": ["prompt"]
    }
  }
]

# 음향감독 클래스
class SoundDirector(Role):
  def __init__(self, model):
    super().__init__([{ "role": "system", "content": instruction }], functions)
    self.model = model

  def create(self, requirements, directory):
    result = self.interact(f"""
      {requirements}
      Please create background music that fits the requirements.
    """)

    if result.get("function") == "create":
      prompt = result.get('args').get('prompt')
      print(f"Requirement of BGM : {prompt}")
      return prompt
    else:
      raise Exception("Background music is not created.")
