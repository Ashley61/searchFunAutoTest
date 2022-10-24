import pytest
import os


"""
执行ui自动化
"""
pytest.main(["E:\ANU课程\searchAutoTest\cases\searchTest.py",
             "-sv","--alluredir","./report/temp_jsonreport"])
os.system("allure generate ../report/temp_jsonreport -o ./report/html --clean")