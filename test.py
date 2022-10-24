# _* coding: utf-8 _*_
# _author_:zeng
# 2020/7/31_10:02

"""百度接口测试(get方法)"""
import requests
import unittest
params = {"kw": "python", "fr": "search"}
response = requests.get('http://baidu.com/',params)
print(response.status_code)
#
# class TeiBa(unittest.TestCase):
#     def setUp(self):
#         # 测试的url
#         # https://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search
#         self.url = "https://tieba.baidu.com/f?"
#         # 需要传递的参数
#         self.params = {"kw": "python", "fr": "search"}
#
#         # 添加请求头，模拟浏览器访问
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
#         }
#         # 发送get请求
#         self.r = requests.get(self.url, params=self.params, headers=self.headers)
#
#     # 编写一个测试用例，判断请求是否成功，是否包含搜索关键字
#     def test_tieba(self):
#         print("开始测试百度贴吧搜索接口")
#         respones = self.r.text
#         # 断言状态码是否为200
#         self.assertEqual(self.r.status_code, 200)
#         # 判断返回内容是否包含所搜关键词
#         self.assertIn('python', respones)
#         # print(self.r.status_code)
#         print("测试通过")
#
#     def tearDown(self):
#         print("一条测试用例执行完成！！！")
#
#
# if __name__ == '__main__':
#     unittest.main()
