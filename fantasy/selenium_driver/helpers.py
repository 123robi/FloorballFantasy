from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def install_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--lang=en")
    options.add_argument("window-size=1920,1080")
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


def find_element(driver, method, element_locator):
    wait_until(driver, EC.element_to_be_clickable((method, element_locator)))
    return driver.find_element(method, element_locator)


def wait_until(driver, method, delay=5):
    WebDriverWait(driver, delay).until(method)


def get_parent(element):
    return element.find_element_by_xpath('..')
