from dotenv import load_dotenv
from packages.roles import Director
from packages.manager import Manager

load_dotenv()

def main():
  director = Director()
  number_of_scene = director.configure_advertisement("iPhone")
  manager = Manager(number_of_scene)

  for scene_number in range(1, manager.num_of_scene + 1):
    requirements = director.create_requirements_by_scene(scene_number)
    manager.register_scene_requirements(scene_number, requirements)
    scene = manager.create_scene(scene_number)
  
  print(manager.requirements)

if __name__ == "__main__":
  main()