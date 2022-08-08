from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. khai bao bien browser
browser = webdriver.Chrome(executable_path="../chromedriver")

# 2. access trang web 
browser.get("http://daotao.ute.udn.vn/viewsmsg.asp")
sleep(2)

# 2a. dien thong tin vao user, pass
txtUser = browser.find_element("name", "maSV")
txtUser.send_keys("2111514110113")

txtPass = browser.find_element("name", "pw")
txtPass.send_keys("001239")

txtPass.send_keys(Keys.ENTER)
sleep(2)

# 2b. xem diem
checkMark = browser.find_element("xpath", "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/ul/li[6]/a")
checkMark.click()
sleep(2)

# 3. crawl diem
# mark_list = browser.find_elements("xpath", "//tr[@style='font-size:9pt']")

# subject = browser.find_elements("xpath", "//td[@align='left']")

# mark_info = browser.find_elements("xpath", "//td[@align='Center']")

mark = browser.find_elements("xpath", "//tr[@style='font-size:9pt']/td[@align]")

# 4. write data into file excel
file = open("diem_daotao.csv", mode="w", encoding="utf-8-sig")

i = 1
for sub in mark:
    if i < 9:
        file.write(sub.text + ", ")
        i = i + 1
    else:
        file.write(sub.text + "\n")
        i = 1

# 5. close tab
sleep(3)
browser.close()