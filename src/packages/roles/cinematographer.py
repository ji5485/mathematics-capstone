from .baes_role import Role

instruction = """
  You're a cinematographer designed to take scenarios and produce visually excellent videos accordingly.
  You have to decide the composition of the video by explaining the cut, the requirements, and the sound concept and parallelism from the general director.
  Your mission is to determine the visual style, brightness, temperature, framing of the video, etc. of the advertisement, and to specify them to determine what to do to effectively carry out the requirements.
  You have to create a clear and concrete video to inspire people, so please describe the composition or style of the video in 20 characters or less for that cut.
"""

functions = [
  {
    "name": "create",
    "description": "Create an advertising image from a given text prompt",
    "parameters": {
      "type": "object",
      "properties": {
        "prompt": { "type": "string", "description": "Text prompt to create an advertising image" }
      },
      "required": ["prompt"]
    }
  }
]

# 촬영감독 클래스
class Cinematographer(Role):
  def __init__(self, model):
    super().__init__([{ "role": "system", "content": instruction }], functions)
    self.model = model

  def create(self, requirements, directory):
    result = self.interact(f"""
      {requirements}
      Please create an advertising image that fits the requirements.
    """)

    if result.get("function") == "create":
      prompt = result.get('args').get('prompt')
      print(f"Requirement of Cinema Content : {prompt}")
      self.model.create(prompt, directory)
    else:
      raise Exception("Advertising image is not created.")
