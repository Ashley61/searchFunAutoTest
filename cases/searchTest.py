from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import yaml
import allure
import time
import os

"""
百度搜索功能UI自动化case
"""

@allure.testcase("搜索功能")
@pytest.mark.parametrize('test_data',['selenium','allure'])
def test_SearchFun(test_data):

    with open("help.yaml", encoding='utf-8') as file:
        data = yaml.safe_load(file)

    with allure.step('step one:打开chrome输入网址'):
        wd = webdriver.Chrome(executable_path=data["chromeDriver"])
        wd.get('https://www.baidu.com')

    with allure.step('step two:搜索栏输入data并点击搜索'):
        wd.find_element_by_id('kw').send_keys(test_data)
        time.sleep(2)
        wd.find_element_by_id('su').click()
        time.sleep(5)

    #class name定位
    elements=wd.find_elements_by_class_name("bk_polysemy_1Ef6j")

    #判断结果是否和搜索有关
    if (test_data in (elements[0].text)):
        print("success")

    #截屏当前浏览器内容
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    wd.get_screenshot_as_file('./report/'+now+'.png')

    with allure.step('step four:关闭浏览器，退出'):
        wd.quit()

#
#
# if __name__ =="__main__":
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /report2 目录
#     pytest.main(['--alluredir', '../report/result'])
#     # 执行命令 allure generate ./report2 -o ./report2 --clean ，生成测试报告
#     os.system('allure generate ../report/result -o  ../report/html --clean')