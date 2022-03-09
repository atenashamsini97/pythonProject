from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
## address site
driver.get("https://www.amazon.com")
print(driver.title)
driver.maximize_window()
driver.close()



search = driver.find_element('id','nav-link-accountList-nav-line-1').click()
search2 = driver.find_element('id','ap_email')
search2.send_keys("mahdiyeshamsini97@gmail.com")
search3 = driver.find_element('id','continue').click()


search3 = driver.find_element('id','createAccountSubmit').click()
search5 = driver.find_element('id','ap_customer_name')
search5.send_keys("shamsini")
search4 = driver.find_element('id','ap_password')
search4.send_keys("1234aaa")
search7 = driver.find_element('id','ap_email')
search7.send_keys("mahdiyeshamsini97@gmail.com")
search6 = driver.find_element('id','ap_password_check')
search6.send_keys("1234aaa")
check= driver.find_element('id','continue').click()
#search4.send_keys(Keys.RETURN)
#driver.get(f"{base_url}/login.html")
#driver.find_element('ClassName','VfPpkd-vQzf8d').click()
#check= driver.find_element('id','check_validate').text
#assert check=='PYTHON'
#driver.find_element('id','notes').send_keys("hello world shbn ij uee jdikj je4 dfoj")
#check2=driver.find_element('id','area_notes_validate').text
#assert check2=='hello world shbn ij uee jdikj je4 dfoj'


