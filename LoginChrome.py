from selenium import 
driver=webdriver.Chrome("D:\\Selenium\\Drivers\\chromedriver.exe")
driver.get("http://www.gmail.com")
driver.find_element_by_id("Email").send_keys("vasanthmuthu")
driver.find_element_by_id("next").click()
driver.implicitly_wait(50)
driver.find_element_by_id("Passwd").send_keys("sdsdsd")
driver.find_element_by_id("signIn").click()
