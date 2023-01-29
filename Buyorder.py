from selenium import webdriver
from selenium.webdriver.common.by import By

def buyorder(driver,low):
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
