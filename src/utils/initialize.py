import openai
from .constants import OPENAI_API_KEY

def initialize():
  openai.api_key = OPENAI_API_KEY