from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 阿洁听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get("http://127.0.0.1:8000")

        # 她注意到网页的标题和头部包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 应用邀请她输入一个待办事项

        # 她在文本框中输入了"Buy peacock feathers"
        # 阿洁的爱好是使用假蝇做饵钓鱼
        # 她按回车键后，页面更新了
        # 待办事项表格中显示了“1: Buy peacock feathers”

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了“Use peacock feathers to make a fly(”使用孔雀羽毛做假蝇)
        # 伊迪丝做事很有条理
        # 页面再次更新，她的清单中显示了这两个待办事项
        # 伊迪丝想知道这个网站是否会记住她的清单

        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能
        # 她访问那个URL，发现她的待办事项列表还在
        # 她很满意，去睡觉了

if __name__ == '__main__':
    unittest.main()
