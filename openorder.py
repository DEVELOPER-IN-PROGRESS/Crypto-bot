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

