from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.mouse_button import MouseButton
import time
import gc

driver = webdriver.Firefox()
driver.get('https://accounts.binance.com/en/login?return_to=aHR0cHM6Ly93d3cuYmluYW5jZS5jb20vZW4vdHJhZGUvQlRDX1VTRFQ_dGhlbWU9ZGFyayZ0eXBlPXNwb3Q%3D')

recorded_low = 0
recorded_high = 0

avg_price = 0

def passcheck():
     while True:
          user_input = input("Enter the key:")
          if user_input == "keys":
               print(" correct !")
               break
          else:
               print("Try again.")

buy_price = 0
sell_price = 0

def cancel_all():
     print('order cancelled')
     try:
          cross = driver.find_elements(By.CSS_SELECTOR,'.css-19tho47')
          for e in cross:
            e.click()
     except:
          print('no crosses')
     driver.find_element(By.ID,'cancel-all-orders').click()
     time.sleep(0.2)
     try:
          overlay = driver.find_element(By.CSS_SELECTOR,'.css-1u2pn8e')
          driver.execute_script("arguments[0].style.position = 'static'", overlay )
          button = driver.find_element(By.CSS_SELECTOR,'.css-tzcjm7')
          driver.execute_script("arguments[0].style.position = 'fixed'", button )
          driver.execute_script("arguments[0].style.top = '40%'", button )
          driver.execute_script("arguments[0].style.zIndex = '10000'", button )
          driver.find_element(By.CSS_SELECTOR,'.css-bsagu5').click()
     except:
          print('overlay fail')

def open_check(order):
     start_time = time.time()
     while True:
          try:
            driver.find_element(By.CSS_SELECTOR,'.css-j0mvbd')
            break
          except:
               time.sleep(9)

          global avg_price
          avg_price = float(driver.find_element(By.CSS_SELECTOR,'.contractPrice').text.replace(',',''))

          # if order == "buy" and buy_price - avg_price < 10:
          #      cancel_all()
          #      buyorderplace(avg_price)

          if time.time() - start_time > 69.0 :
               print('timeout 😥 do something ')
               if order == "buy" :
                    cancel_all()
                    buyorderplace(avg_price)
                    return
     return

def buyorderplace(low):
     print('inside Buy order')
     curr_low = float(driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-bid  .orderbook-progress:nth-child(6) .bid-light').text)
     print("current low {}".format(curr_low))
     # high_point = driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-ask  .orderbook-progress:nth-child(2) .ask-light').text
     walletcash =  driver.find_elements(By.CSS_SELECTOR,'.css-k4h8bj')

     curr_low = min(curr_low,low)
     buy = driver.find_element(By.ID,'FormRow-BUY-price')
     buy.clear()
     buy.send_keys(curr_low)
     # buy.send_keys(curr_low)
     global buy_price
     buy_price = curr_low

     print("Price at buying {}".format(buy_price))

     available_usdt =  walletcash[0].text.split(' ')[0]
     orderplace = driver.find_element(By.ID,'FormRow-BUY-total')
     orderplace.clear()
     orderplace.send_keys(available_usdt)
     driver.find_element(By.ID,'orderformBuyBtn').click()
     open_check("buy")

def sellorderPlace(high):
     print('inside sell order')
     # low_point = driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-bid  .orderbook-progress:nth-child(15) .bid-light').text
     curr_high = float(driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-ask  .orderbook-progress:nth-child(3) .ask-light').text)
     walletcash =  driver.find_elements(By.CSS_SELECTOR,'.css-k4h8bj')

     start = time.time()
     # Sell code
     high_point = float(max(curr_high,high))
     while high_point - buy_price <= 4.0 :
          high_point = float(driver.find_element(By.CSS_SELECTOR,'.contractPrice').text.replace(',',''))

          diff = buy_price - high_point
          if time.time() - start > 269 and (diff > 10 and diff < 20):
               cancel_all()
               open_check("sell")
               sellorderPlace(high_point)
          time.sleep(1)

     sell = driver.find_element(By.ID,'FormRow-SELL-price')
     sell.clear()
     sell.send_keys(high_point)

     available_btc = walletcash[1].text.split(' ')[0]
     print(available_btc,'btc')

     sellplace = driver.find_element(By.ID,'FormRow-SELL-quantity')
     sellplace.clear()
     sellplace.send_keys(available_btc)
     driver.find_element(By.ID,'orderformSellBtn').click()
     open_check("sell")

if __name__ == '__main__':
     footer = driver.find_element(By.CSS_SELECTOR,'.footer-sticky')
     driver.execute_script("arguments[0].style.position = 'static'", footer )
     driver.execute_script("arguments[0].style.zIndex = '0'", footer )
     count = 0

     for i in range(0,13):
          low_point = float(driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-bid  .orderbook-progress:nth-child(4) .bid-light').text)
          high_point = float(driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-ask  .orderbook-progress:nth-child(6) .ask-light').text)
          print(" global record low {}  ".format(recorded_low))
          recorded_low = low_point
          print(" current record low {} iteration {} ".format(recorded_low , i))
          buyorderplace(low_point)
          sellorderPlace(high_point)
          if i % 5 == 0 :
               gc.collect()