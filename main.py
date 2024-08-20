from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from fake_useragent import UserAgent

def _nameparser(url):
        lst = url.split('/')[-1].replace('-',' ')
        return lst

url = input('Send me ur link: ')


options = Options()
options.add_argument(f"user-agent={UserAgent.random}")
options.add_argument('--headless')
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get(url)

try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'Lyrics__Container-sc-1ynbvzw-1'))
    )

    lyrics = "\n".join([element.text for element in elements])

    with open(f'{_nameparser(url)}.txt', 'w', encoding='utf-8') as f:
        f.write(lyrics)

except TimeoutException:
    print("Items not found within the set time limit")
