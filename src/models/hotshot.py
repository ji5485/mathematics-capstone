import requests
import os
from selenium.webdriver.common.by import By
from seleniumbase import Driver

driver = Driver(uc=True)

class Hotshot:
  def __init__(self, requestId):
    self.requestId = requestId

  def generate(self, command):
    self.login()

    driver.type('textarea#main-search-box', command, timeout=100)
    driver.click('button:contains("go")')
    driver.click('span:contains("Your GIFs are ready")', timeout=100)
    img = driver.find_element(By.ID, "main-image-preview")
    img_src = img.get_attribute('src')

    return self.download(img_src)

  def login(self):
    driver.open('https://hotshot.co/login')
    driver.type('input#identifierId', os.environ.get("GOOGLE_EMAIL"))
    driver.click('span:contains("Next")')
    driver.type('input[type="password"]', os.environ.get("GOOGLE_PASSWORD"))
    driver.click('span:contains("Next")')

  def download(self, link):
    filename = os.path.basename(link)
    position = os.path.join(os.getcwd(), 'artifacts', self.requestId, filename)

    with open(position, 'wb') as gif_file:
      gif_response = requests.get(link)
      gif_file.write(gif_response.content)

    return filename
