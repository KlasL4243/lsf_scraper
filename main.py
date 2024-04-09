from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

username = "inf4143"
password = "S*Vr5XUDpCi@iSdu"

link_home = "https://lsf.hs-worms.de/"
link_plan = "https://lsf.hs-worms.de/qisserver/rds?state=wplan&act=show&pool=&show=plan&P.vx=lang&P.subc=plan"

driver = Chrome()

driver.get(link_home)

form = driver.find_element(By.NAME, "loginform")

input_username = driver.find_element(By.ID, "asdf")
input_password = driver.find_element(By.ID, "fdsa")

input_username.send_keys(username)
input_password.send_keys(password)

form.submit()

driver.get(link_plan)

status_bar = driver.find_element(By.CLASS_NAME, "divloginstatus")

if "Logout" not in status_bar.text:
    print("Login failed!")
    
