driver_path = r"YOUR_CHROME_DRIVER_PATH"
import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
lyrics = []

class Lyrics_Scraping:
    def __init__(self,song,artist):
        global lyrics
        self.url = 'https://www.google.com'
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(self.url)
        self.search = self.driver.find_element_by_class_name('gLFyf')
        self.search.click()
        self.search.send_keys(f'{song} {artist} lyrics')
        self.search.send_keys(Keys.ENTER)
        time.sleep(2)
        self.lyrics = self.driver.find_elements_by_css_selector(("span[jsname='YS01Ge']"))
        for l in self.lyrics:
            lyrics.append(l.text)

    def get_lyrics(self):
      self.driver.quit()
      return lyrics












