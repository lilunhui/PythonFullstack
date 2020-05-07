from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import  webdriver
import selenium

url = 'http://www.maiziedu.com/'
login_text = '登录'
account = 'abc123456'
pwd = 'abc123456'

def get_ele_time(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def login_test():
    d = webdriver.Chrome()
    d.get(url)

    d.maximize_window()
    ele_login = get_ele_time(d,10, lambda d: d.find_element_by_link_text(login_text))
    ele_login.click()
    account_ele = d.find_element_by_id('id_account_1')
    account_ele.send_keys('')
    account_ele.click()

    account_ele.send_keys(account)
    pwd_ele = d.find_element_by_id('id_password_1')
    pwd_ele.clear()
    pwd_ele.send_keys(pwd)
    d.find_element_by_id('login_btn').click()

    try:
        d.find_element_by_link_text('该账号格式不正确')
        print('Account And Pwd Error!')
    except:
        print('Account And Pwd Right!')
if __name__ == '__main__':
    login_test()



