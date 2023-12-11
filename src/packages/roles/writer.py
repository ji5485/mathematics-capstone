from .baes_role import Role

instruction = """
  You are a writer who understands the main concepts and themes and develops stories and scenarios for advertising.
  You should take the scenario you received from the general director and write the dialogue, narration, or text elements needed for the scenario and incorporate them into the scenario.
  It creates a powerful and moving story that draws people's attention and provides a foundation for achieving the goal,
  The goal is to write concise and effective conversations or phrases that fit the topic and deliver a clear message to people.
  It will also determine the tone and atmosphere of the advertisement and communicate it through scenarios,
  At this time, the tone and atmosphere should be related to the product or brand identity of the advertisement and should match the theme.
  Please understand the target audience group and write content for effective message delivery.
"""

functions = [
  {
    "name": "create",
    "description": "Create a narration from a given text prompt",
    "parameters": {
      "type": "object",
      "properties": {
        "prompt": { "type": "string", "description": "Text prompt to create a narration" }
      },
      "required": ["prompt"]
    }
  }
]

# 작가 클래스
class Writer(Role):
  def __init__(self, model):
    super().__init__([{ "role": "system", "content": instruction }], functions)
    self.model = model

  def create(self, requirements, directory):
    result = self.interact(f"""
      {requirements}
      Please write a narration up to 10 words that fits the requirements and create a narration.
    """)

    if result.get("function") == "create":
      prompt = result.get('args').get('prompt')
      print(f"Narration : {prompt}")
      return prompt
    else:
      raise Exception("Narration is not created.")