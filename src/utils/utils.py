import os

def createDirectory(requestId):
  try:
    if not os.path.exists(f"{os.getcwd()}/artifacts/{requestId}"):
      os.makedirs(f"{os.getcwd()}/artifacts/{requestId}")
  except OSError:
    pass