from selenium import webdriver
from time import time

driver = webdriver.Remote(
   command_executor='http://selenium-hub:4444/wd/hub',
   desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

start_time = time()
driver.get('http://ifconfig.me')
end_time = time()
response_time = end_time - start_time

print("Response Time: ", response_time)

driver.quit()

