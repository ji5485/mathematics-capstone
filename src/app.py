from dotenv import load_dotenv
load_dotenv()

from packages.roles import Director
from packages.manager import Manager, Creator

def main():
  director = Director()
  number_of_scene = director.configure_advertisement("Harvard University")
  manager = Manager(number_of_scene)
  creator = Creator(manager.request_id)

  for scene_number in range(1, number_of_scene + 1):
    requirements = director.create_requirements_by_scene(scene_number)
    manager.register_scene_requirements(scene_number, requirements)
    manager.create_scene_artifacts(scene_number)
    creator.create_scene_clip(scene_number)
  
  creator.create_advertisement()

if __name__ == "__main__":
  main()