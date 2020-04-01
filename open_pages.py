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
  sleep_time = 60 * 5 * len(links)
  print(f'Browser will automatically close after {sleep_time / 60} minutes')
  sleep(sleep_time)


def find_links(browser, oz_url):
    browser.get(oz_url)
    elements = browser.find_elements_by_xpath('//*[@id="main"]/div[1]/div')

    links = []
    for ele in elements:
        try:
            words = ele.text
            if "Purchase" not in words and "Today" in words:
                links.append(ele.find_element_by_tag_name('a').get_attribute('href'))
        except NoSuchElementException:
            pass
    return links




options = Options()
options.add_argument('--headless')

options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')

if platform.system() == 'Windows':
    browser = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
else:
    browser = webdriver.Chrome(executable_path='./chromedriver', options=options)

total_links = []
i = 0
first_page = 'https://www.ozbargain.com.au/competition/closing'
next_pages = 'https://www.ozbargain.com.au/competition/closing?page={}'
while True:
    if i == 0:
        links = find_links(browser, first_page)
    else:
        links = find_links(browser, next_pages.format(i))
    if len(links) == 0:
        break
    else:
        total_links += links
    i += 1

browser.quit()
print(total_links)
open_window(total_links)
