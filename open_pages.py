from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import platform
from os.path import expanduser

def open_window(links):
  options = Options()
  options.add_argument('--ignore-certificate-errors')
  options.add_argument('--no-sandbox')
  home_path = expanduser('~')
  if platform.system() == 'Windows':
      options.add_argument("user-data-dir={}/AppData/Local/Google/Chrome/User Data/Profile 2".format(home_path))
  else:
      options.add_argument("user-data-dir={}/Library/Application Support/Google/Chrome/User Data/Profile 2".format(home_path))

  browser = webdriver.Chrome(executable_path='./chromedriver', options=options)
  browser.maximize_window()
  browser.get(links[0])
  i = 1
  while i < len(links):
    browser.execute_script('''window.open("http://google.com","_blank");''')
    browser.switch_to.window(browser.window_handles[i])
    browser.get(links[i])
    i += 1
  sleep(60 * 10)



options = Options()
options.add_argument('--headless')

options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

if platform.system() == 'Windows':
    browser = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
else:
    browser = webdriver.Chrome(executable_path='./chromedriver', options=options)
browser.get('https://www.ozbargain.com.au/competition/closing')

elements = browser.find_elements_by_xpath('//*[@id="main"]/div[1]/div')

links = []
for ele in elements:
    try:
        words = ele.text
        if "Purchase" not in words and "Today" in words:
            links.append(ele.find_element_by_tag_name('a').get_attribute('href'))
    except NoSuchElementException:
        pass

browser.quit()
print(links)
open_window(links)