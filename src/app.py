from dotenv import load_dotenv
load_dotenv()

from packages.roles import Director
from packages.manager import Manager, Creator

request_id = "a637292d-f625-466d-b29e-ffb40f6cd428"

def main():
  # director = Director()
  # number_of_scene = director.configure_advertisement("iPhone")
  # manager = Manager(number_of_scene)
  # creator = Creator(manager.request_id)
  creator = Creator(request_id)

  for scene_number in range(1, 4):
    # requirements = director.create_requirements_by_scene(scene_number)
    # manager.register_scene_requirements(scene_number, requirements)
    # manager.create_scene_artifacts(scene_number)
    creator.create_scene_clip(scene_number)
  
  creator.create_advertisement()
  # print(manager.requirements)

if __name__ == "__main__":
  main()