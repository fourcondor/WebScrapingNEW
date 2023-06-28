from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

if __name__ == '__main__':
    for i in  range(0,3):
        # Imposta le opzioni del browser per gestire i cookie
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-notifications')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        driver.get("https://www.covermanager.com/reservation/module_restaurant/restaurante-celebritiesgold-puertobanus/english")

        # Attendi fino a quando il banner dei cookie è visibile
        # wait = WebDriverWait(driver, 10)
        # cookie_banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 't972__banner')))
        #
        # # Accetta il banner dei cookie
        # accept_button = cookie_banner.find_element(By.CLASS_NAME, 't972__accept-btn')
        # accept_button.click()

        # Attendi fino a quando il pulsante "Group request" è visibile
        wait = WebDriverWait(driver, 10)
        group_request_button = wait.until(EC.visibility_of_element_located((By.ID, 'group_request_button')))

        # Fai clic sul pulsante "Group request"
        group_request_button.find_element(By.CLASS_NAME, 'form-control.step1').click()

        input_element = driver.find_element(By.ID, "user_first_name")
        input_element.send_keys("ATTACKKK")

        second_element = driver.find_element(By.ID, "user_last_name")
        second_element.send_keys("ATTACKKK")

        email_element = driver.find_element(By.ID, "user_email")
        email_element.send_keys("abc@live.com")

        phone_element = driver.find_element(By.ID, "user_phone")
        phone_element.send_keys("3333333333")

        select_element = driver.find_element(By.ID, "extra_people_group_request")
        select = Select(select_element)
        select.select_by_value("20")

        checkbox_element = driver.find_element(By.ID, "no_food_restrictions")
        checkbox_element.click()


        checkbox_element2 = driver.find_element(By.ID, "legal_ficha")
        checkbox_element2.click()
        checkbox_element2 = driver.find_element(By.ID, "consentimiento_legal")
        checkbox_element2.click()
        checkbox_element2 = driver.find_element(By.ID, "subscribe_newsletter")
        checkbox_element2.click()

        button = driver.find_element(By.CSS_SELECTOR, 'input[value="Request"].reservarButton')
        button.click()

        # Puoi inserire altre azioni dopo aver cliccato sul pulsante

        time.sleep(10)
        driver.quit()
