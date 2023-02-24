import os
from selenium import webdriver


def checkchrome_version(chromepath):
    webdriver_version = webdriver.__version__
    print(webdriver_version)
    os.chdir(chromepath)
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
            print(current_version)
        else:
            pass

        loop_inital += 1


if __name__ == '__main__':
    chromepath = r'C:\Program Files\Google\Chrome\Application'
    checkchrome_version(chromepath)
