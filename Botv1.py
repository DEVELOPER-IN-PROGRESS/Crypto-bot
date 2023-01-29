import Buyorder as BO
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import gc

driver = webdriver.Firefox()
driver.get('https://accounts.binance.com/en/login?return_to=aHR0cHM6Ly93d3cuYmluYW5jZS5jb20vZW4vdHJhZGUvQlRDX1VTRFQ_dGhlbWU9ZGFyayZ0eXBlPXNwb3Q%3D')
avg_price = 0

def passcheck():
     while True:
          user_input = input("Enter the key:")
          if user_input == "keys":
               print(" correct !")
               break
          else:
               print("Try again.")

if __name__ == '__main__':
    passcheck()
    footer = driver.find_element(By.CSS_SELECTOR,'.footer-sticky')
    driver.execute_script("arguments[0].style.position = 'static'", footer )
    driver.execute_script("arguments[0].style.zIndex = '0'", footer )
    count = 0

    avg_price = float(driver.find_element(By.CSS_SELECTOR,'.contractPrice').text.replace(',',''))
    BO.buyorder(driver,avg_price)
