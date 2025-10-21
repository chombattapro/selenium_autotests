from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    pre_button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    if pre_button == True:
        button1 = browser.find_element(By.ID, "book").click()

    button = browser.find_element(By.TAG_NAME, "button")

    """под вопросом"""
    # пролистываем страницу до состояния когда ФУТЕР(нижний блок сайта) не перекрывает найденную нами кнопку
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    last_button = browser.find_element(By.ID, "solve")
    last_button.click()

finally:
    time.sleep(5)
    browser.quit()

# - Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
#
# - Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился,
# то получим StaleElementReferenceException.
# Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click.
# Если кнопка за это время была скрыта скриптом,
# то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
#
# - Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры),
# и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.