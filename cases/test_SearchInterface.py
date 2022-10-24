import pytest
import yaml
import allure
import os
import requests

"""
百度搜索接口自动化
"""
def setup_function():
    print ("begin")


def teardown_function():
    print ("end")

def search_function(data):
    param = {"kw": data, "fr": "search"}
    return  requests.get('http://baidu.com/', param)


@allure.feature('百度搜索')
def test_English_search():
    res= search_function("python")
    print("英文输入搜索：", res.status_code)
    assert res.status_code==200


@allure.feature('百度搜索')
def test_chinese_search():
    res = search_function("自动化测试")
    print("中文输入搜索：", res.status_code)
    assert res.status_code==200


@allure.feature('百度搜索')
def test_noCondition_search():
    res = search_function("")
    print("无条件输入搜索：", res.status_code)
    assert res.status_code==200


@allure.feature('百度搜索')
def test_containSpace_search():
    res=search_function("Australian National University")
    print("含空格输入搜索：", res.status_code)
    assert res.status_code == 200


@allure.feature('百度搜索')
def test_number_search():
    res = search_function(1234)
    print("含数字输入搜索：", res.status_code)
    assert res.status_code == 200


@allure.feature('百度搜索')
def test_symbol_search():
    res = search_function("zhangsan@163.com")
    print("含特殊字符输入搜索：", res.status_code)
    assert res.status_code == 200


@allure.feature('百度搜索')
def test_longContent_search():
    res = search_function("HelloWorld1234567890123456789qwertyuiopasdfghjklqwertyuioasdfghjklzxcvbnmxcvbnmzxcvbnmasdfgh")
    print("过长输入搜索：", res.status_code)
    #状态码200，自动截取字符串长度去搜索
    assert res.status_code == 200

@allure.feature('百度搜索')
def test_null_search():
    res = search_function(data=None)
    print("none输入搜索：", res.status_code)
    assert res.status_code == 200



if __name__ =="__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /report2 目录
    pytest.main(['--alluredir', './report2/report/result'])
    # 执行命令 allure generate ./report2 -o ./report2 --clean ，生成测试报告
    os.system('allure generate ./report2/report/result -o  ./report2/report/html --clean')