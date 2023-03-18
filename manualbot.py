from selenium import webdriver
from selenium.webdriver.common.by import By
from binance.spot import Spot
import env
import time
import gc

driver = webdriver.Firefox()
driver.get('https://accounts.binance.com/en/login?return_to=aHR0cHM6Ly93d3cuYmluYW5jZS5jb20vZW4vdHJhZGUvQlRDX1VTRFQ_dGhlbWU9ZGFyayZ0eXBlPXNwb3Q%3D')
client = Spot(env.API_KEY, env.API_SECRET)

available = 1430

def passcheck():
     while True:
          user_input = input("Enter the key:")
          if user_input == "keys":
               print(" correct !")
               break
          else:
               print("Try again.")

def buyorder():
     print('inside Buy order')
     curr_low = float(driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-bid  .orderbook-progress:nth-child(3) .bid-light').text)
     # print("current low {}".format(curr_low))
     # high_point = driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-ask  .orderbook-progress:nth-child(2) .ask-light').text
     walletcash =  driver.find_elements(By.CSS_SELECTOR,'.css-k4h8bj')

     buy = driver.find_element(By.ID,'FormRow-BUY-price')
     buy.clear()
     buy.send_keys(curr_low)
     # buy.send_keys(curr_low)

     available_usdt =  walletcash[0].text.split(' ')[0]
     orderplace = driver.find_element(By.ID,'FormRow-BUY-total')
     orderplace.clear()
     orderplace.send_keys(available_usdt)
     driver.find_element(By.ID,'orderformBuyBtn').click()

     global available
     available = available_usdt
     print ('order bought placed at ', available_usdt )

def sellorderPlace():
     print('inside sell order')

     curr_high = float(driver.find_element(By.CSS_SELECTOR,'.orderbook-list.orderbook-ask  .orderbook-progress:nth-child(1) .ask-light').text)
     walletcash =  driver.find_elements(By.CSS_SELECTOR,'.css-k4h8bj')

     high_point = curr_high

     sell = driver.find_element(By.ID,'FormRow-SELL-price')
     sell.clear()
     sell.send_keys(high_point)

     available_btc = walletcash[1].text.split(' ')[0]
     print(available_btc,'btc')
     print('sold at' , high_point)

     print('available cash ' , available )

     sellplace = driver.find_element(By.ID,'FormRow-SELL-quantity')
     sellplace.clear()
     sellplace.send_keys(available_btc)
     driver.find_element(By.ID,'orderformSellBtn').click()

if __name__ == '__main__':
     passcheck()
     footer = driver.find_element(By.CSS_SELECTOR,'.footer-sticky')
     driver.execute_script("arguments[0].style.position = 'static'", footer )
     driver.execute_script("arguments[0].style.zIndex = '0'", footer )
     count = 0

     while True:
           operation = input("operation: ?")
           if operation == 'b' :
                buyorder()
           elif operation == 's' :
                sellorderPlace()
           elif operation =='c':
                client.cancel_open_orders("BTCUSDT")

           count = count + 1

           if count % 20 == 0:
                gc.collect()




