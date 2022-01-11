
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://bbs.51testing.com/forum.php")

sleep(3)

driver.find_element_by_id("ls_username").send_keys("DeemoA")
driver.find_element_by_id("ls_password").send_keys("19980117lbvae")
txt = driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').text

# 打印获取的文本
print(txt)

# 定位“登录”按钮并获取登录按钮的type属性值
type = driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').get_attribute("type")

# 打印type属性值
print(type)

# 定位“登录”按钮并进行点击操作
driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').click()

sleep(3)
driver.quit()
