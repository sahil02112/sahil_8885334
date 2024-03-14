from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")

try:
    # Waiting for the bed link to be clickable
    bed_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[3]")))
    bed_link.click()

    time.sleep(5)


    # Waiting for the first bed link to be clickable
    bed1_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/ol/li[1]/div/div[2]/div/a[2]/span/div")))
    bed1_link.click()

    time.sleep(5)

    bed1_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[2]/div[1]/div/div[7]/div[1]/div[2]/div[2]/div/div/div[1]/div[20]/div[1]/div/form/div/ul/li[3]/span/div/span/span/span/button/div/div[1]/img")))
    bed1_link.click()

    time.sleep(5)

    bed1_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[2]/div[1]/div/div[7]/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div/ul/li[2]/a/div/div/span")))
    bed1_link.click()

    time.sleep(5)



except TimeoutException:
    print("The bed link or the first bed link could not be found within the specified time.")

# Closing the webdriver
driver.quit()
