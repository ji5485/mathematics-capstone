import os
import uuid
from packages.roles import Writer, SoundDirector, Cinematographer
from packages.models import DallE

class Manager:
  def __init__(self, num_of_scene):
    self.num_of_scene = num_of_scene
    self.requirements = {}
    self.request_id = str(uuid.uuid4())

    self.workers = {
      "writer": Writer(DallE()),
      "sound_director": SoundDirector(DallE()),
      "cinematographer": Cinematographer(DallE())
    }

  def register_scene_requirements(self, scene_number, requirements):
    self.requirements[scene_number] = requirements

  def create_scene_artifacts(self, scene_number):
    directory = os.path.join(os.getcwd(), "src", "artifacts", self.request_id, f"scene-{scene_number}")

    if not os.path.exists(directory):
      os.makedirs(directory)

    for [key, worker] in self.workers.items():
      worker.create(self.requirements.get(scene_number).get(key), directory)

    print(f"Scene {scene_number} created successfully!")
