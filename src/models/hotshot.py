import requests
import os
from selenium.webdriver.common.by import By
from seleniumbase import Driver
from utils.utils import createDirectory

class Hotshot:
  def __init__(self, requestId):
    self.requestId = requestId
    self.driver = Driver(uc=True)

  # Command를 입력받아 Hotshot에서 GIF를 생성하는 메서드
  def generate(self, command):
    self.login()

    self.driver.type('textarea#main-search-box', command, timeout=100)
    self.driver.click('button:contains("go")')
    self.driver.click('a:contains("Copy GIF Link")', timeout=100)
    img = self.driver.find_element(By.ID, "main-image-preview")
    img_src = img.get_attribute('src')

    return self.download(img_src)

  # 구글 로그인 메서드
  def login(self):
    self.driver.open('https://hotshot.co/login')
    self.driver.type('input#identifierId', os.environ.get("GOOGLE_EMAIL"))
    self.driver.click('span:contains("Next")')
    self.driver.type('input[type="password"]', os.environ.get("GOOGLE_PASSWORD"))
    self.driver.click('span:contains("Next")')

  # GIF를 다운로드하는 메서드
  def download(self, link):
    createDirectory(self.requestId)
    file_name = os.path.basename(link)
    position = os.path.join(os.getcwd(), 'artifacts', self.requestId, file_name)

    with open(position, 'wb') as gif_file:
      gif_response = requests.get(link)
      gif_file.write(gif_response.content)

    return file_name
