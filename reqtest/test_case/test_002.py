'''
import urllib.request
params = "TomCruise" # 汤姆·克鲁斯的电影
url = "https://api.douban.com/v2/movie/search?"
html = urllib.request.urlopen(url + params) # 通过urllib发起请求
html = html.read().decode("utf-8")
print(html)
'''
import requests ,json
import unittest


class Demo(unittest.TestCase):

        def setUp(self):
            # 初始化信息
            self.url = "https://api.douban.com/v2/movie/search?"
            self.actor_name = "q=TomCruise"
            self.style_tag = "tag=爱情"
            self.name = "汤姆·克鲁斯"
            self.action = "动作"

        def test_actor(self):
            # 执行测试
            req = requests.get(self.url + self.actor_name) # 通过requests 发起请求
            req = json.dumps(req.json(), ensure_ascii=False, indent=4)
            self.assertIn(self.name, req, msg=None) # 检查有没有 "汤姆·克鲁斯"这个演员

        def test_style_tag(self):
            # 执行测试
            req = requests.get(self.url + self.actor_name) # 通过requests 发起请求
            req = json.dumps(req.json(), ensure_ascii=False, indent=4)
            self.assertIn(self.action, req, msg=None) # 检查有没有 "动作片"

if __name__ == '__main__':
    unittest.main()
