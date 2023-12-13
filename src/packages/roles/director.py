from .base_role import Role

instruction = """
  You are a general director designed to produce advertisements.
  The cinematographer, sound director, and writer should be in charge of producing an advertising video that fits the topic presented by the user.
  Your mission is not just to produce videos, but to create ads that are witty and inspiring after looking at your needs from a variety of perspectives.
  You must first specify the subject presented to the user and divide the at least 20-second video into several cuts of at 4 ~ 6 cuts.
  And after you create scenarios for multiple cut edits, you should clearly communicate those scenarios to each model in accordance with the direction of the storyboard.
  Please answer in detail what you will deliver to the photographer, sound director, and writer for each cut.
"""

functions = [
  {
    "name": "configure_number_of_scene",
    "description": "Configure the number of scenes of this advertisement",
    "parameters": {
      "type": "object",
      "properties": {
        "num": { "type": "number", "description": "The number of scene" }
      },
      "required": ["num"]
    }
  },
  {
    "name": "create_requirements_by_scene",
    "description": "Create requirements by scene",
    "parameters": {
      "type": "object",
      "properties": {
        "cinematographer": { "type": "string", "description": "Only description for advertising image" },
        "sound_director": { "type": "string", "description": "Only description of the music to be advertised" },
        "writer": { "type": "string", "description": "Only description of the narration that will go into the ad" }
      },
      "required": ["cinematographer", "sound_director", "writer"]
    }
  }
]

# 총감독 클래스
class Director(Role):
  def __init__(self):
    super().__init__([{ "role": "system", "content": instruction }], functions)

  def configure_advertisement(self, topic):
    result = self.interact(f"The topic of the advertisement is {topic}. Please configure the number of scenes.")

    if result.get("function") == "configure_number_of_scene":
      number_of_scene = result.get("args").get("num")
      print(f"The number of scenes is {number_of_scene}")
      return number_of_scene
    else:
      raise Exception("The number of scenes is not configured.")
  
  def create_requirements_by_scene(self, scene_number):
    result = self.interact(f"Please create requirements by scene {scene_number}.")

    if result.get("function") == "create_requirements_by_scene":
      print(f"Requirements by scene {scene_number} is created successfully")
      return result.get("args")
    else:
      raise Exception(f"Requirements by scene {scene_number} is not configured.")
