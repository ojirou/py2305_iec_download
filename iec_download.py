from selenium import webdriver
from selenium.webdriver.support.select import Select
import os
from time import sleep
os.chdir("C:\\Users\\user\\python\\web_scraping")
current_dir=os.getcwd()
current_dir
tmp_download_dir='C:\\Users\\user\\Downloads'
options=webdriver.ChromeOptions()
prefs={'download.default_directory' : tmp_download_dir}
options.add_experimental_option('prefs',prefs)
driver_path='C:\\Users\\user\\python\\web_scraping\\driver\\chromedriver.exe'
browser=webdriver.Chrome(executable_path=driver_path, chrome_options=options)
url='https://advsearch.iec.ch/ords//f?p=117:104:515448308851839::::FSP_LANG_ID:25'
browser.get(url)
sleep(1)
dropdown=browser.find_element_by_id('DATERANGE_LIST')
select=Select(dropdown)
select.select_by_visible_text('past month')