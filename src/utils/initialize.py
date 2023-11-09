import openai
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

def initialize():
  openai.api_key = os.environ.get("OPENAI_API_KEY")
  return str(uuid.uuid4())