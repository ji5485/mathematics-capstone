import os

def createDirectory(requestId):
  try:
    if not os.path.exists(f"{os.getcwd()}/artifacts/{requestId}"):
      os.makedirs(f"{os.getcwd()}/artifacts/{requestId}")
  except OSError:
    pass
    
def createSceneDirectory():

  path = f"{os.getcwd()}/{director_chat}/{scene_number}"

  for scene_number in range(1, total_scene + 1):
    os.makedirs(path,exist_ok=True)
    os.chdir(path)
