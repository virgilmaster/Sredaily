import time,xlrd,socket
import pyautogui,pyperclip
import paramiko
import subprocess,os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from getpass import getpass


class automation:
    def __init__(self,devops):
        # Write the secret excel file in your computer
        self.filepath = r'C:\example.xlsx'
        self.xlbook = xlrd.open_workbook(self.filepath)
        self.secretdic = {}
        self.devops = devops
        self.jumpserver = 'XXX.XXX.XXX.XXX'
        self.tasks = {
            'build images': self.jenkinslogin,
            "git clone": self.githublogin
        }
        self.chromepath = r'C:\Program Files\Google\Chrome\Application'
        self.chromerui = 'https://chromedriver.storage.googleapis.com/index.html'
        self.browser = webdriver.Chrome()
        
    def main(self):
        self.checkchrome()
        tasker = self.tasks.get(self.devops)
        if tasker:
            tasker()
        else:
            print(f"{tasker} The task name is error")
            import sys
            sys.exit()
        
    
    def checkchrome(self):
        webdriver_version = webdriver.__version__
        print('webdriver version is: ',webdriver_version)
        os.chdir(self.chromepath)
        dir_result = os.listdir()
        dir_loop = len(dir_result)
        loop_inital = 0
        chrome_version_list = ['2','70','72','73','74','75','76','77','78','79','80','81','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113']
    
        while loop_inital < dir_loop:
            convert_res = dir_result[loop_inital]
            inital_split_res = convert_res.split(".")[0]
            convert_version_res = convert_res.split(".")[0:4]

            if inital_split_res in chrome_version_list:
                current_version = str(convert_version_res[0]) + "." +str(convert_version_res[1]) + "." + str(convert_version_res[2]) + "." + str(convert_version_res[3])
                print('Current chrome version is: ',current_version)
            else:
                pass

            loop_inital += 1

    def jenkinslogin(self):
        vpn_result = os.popen('tasklist | findstr "openvpn"')
        con_vpn = vpn_result.readlines()
        vpn_result.close()
        
        # Check the vpn progress
        if con_vpn == []:
            # Edit your vpn path 
            subprocess.run(r'C:\examplevpn.exe')

        else:
            pass
        # Edit you vpn picture
        pic_path = r'D:\Example\python\scanpicture'
        os.chdir(pic_path)
        pic_result = os.listdir()
        
        # Double click terminal
        pic_first = pic_result[0]
        x1,y1 = pyautogui.locateCenterOnScreen(pic_first,confidence=0.9)
        pyautogui.click(x=x1,y=y1,button="left")
        time.sleep(1)

        pic_second = pic_result[1]
        x2,y2 = pyautogui.locateCenterOnScreen(pic_second,confidence=0.9)
        pyautogui.doubleClick(x=x2,y=y2,button="left")
        time.sleep(1)

        # send username arguments
        pyautogui.click(x=1289,y=712,button="left")
        pyperclip.copy('USERNAME')
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        # send passwd arguments
        pyautogui.click(x=1304,y=772,button="left")
        pyperclip.copy('PASSWD')
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pic_third = pic_result[2]
        x3,y3 = pyautogui.locateCenterOnScreen(pic_third,confidence=0.9)
        pyautogui.click(x=x3,y=y3,button="left")
        time.sleep(1)        

        sheetname = self.xlbook.sheets()[0]
        self.secretdic = {}
        username = sheetname.col_values(4)[7]
        password = sheetname.col_values(5)[7]

        initalip = sheetname.col_values(1)[7]
        convertip = str(initalip).split("(")[0]

        initalport = sheetname.col_values(3)[7]
        convertport = str(initalport).split(":")[1]
        
        finalip = "http://" + convertip + ":" + convertport

        self.secretdic['ip'] = finalip
        self.secretdic['username'] = username
        self.secretdic['passwd'] = password
        self.jenkinstask()
      
    def jenkinstask(self):
        ipaddr = self.secretdic['ip']
        username = self.secretdic['username']
        passwd = self.secretdic['passwd']
        print('Current ip address is: ',ipaddr)
        print('Current username is: ',username)
        print('Current password is: ',passwd)
        self.browser.implicitly_wait(10)
        self.browser.get(ipaddr)
        input_username = self.browser.find_element(By.ID,'j_username')
        input_username.send_keys(username)
        input_passwd = self.browser.find_element(By.XPATH,'//input[@name="j_password"]')
        input_passwd.send_keys(passwd)
        self.browser.find_element(By.XPATH,"//button[@name='Submit']").click()
        print('Push forwarding.....')
        time.sleep(10)
    
    def githublogin(self):
        username = 'XXX@gmail.com' # Your username
        password = 'XXXXXXXXXXX' # Your passwd
        self.secretdic['ip'] = 'https://www.github.com/login'
        self.secretdic['username'] = username
        self.secretdic['passwd'] = password
        self.githubtask()

    def githubtask(self):
        ipaddr = self.secretdic['ip']
        username = self.secretdic['username']
        passwd = self.secretdic['passwd']
        self.browser.implicitly_wait(10)
        self.browser.get(ipaddr)
        input_username = self.browser.find_element(By.ID,'login_field')
        input_username.send_keys(username)
        input_passwd = self.browser.find_element(By.ID,'password')
        input_passwd.send_keys(passwd)
        self.browser.find_element(By.CSS_SELECTOR,"input[value='Sign in']").click()


if __name__ == '__main__':
    devops_command = 'jenkins'
    task_name = 'Build images'
    instance1 = automation(devops_command)
    instance1.main()
