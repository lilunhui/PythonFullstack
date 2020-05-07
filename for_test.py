import unittest
from ddt import ddt,unpack,data
from selenium import webdriver

def link():
    lst = []
    with open('pwd.txt','r',encoding='utf-8') as f1:
        for line in f1.readlines():
           lst.append(line.strip('\n').split(','))
    return lst
# print(link())
@ddt
class forTest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    # @data(*link())
    # @unpack
    # def test_1(self,url,txt):
    #     dr = webdriver.Chrome()
    #     dr.get(url)
    #     dr.find_element_by_id('kw').send_keys(txt)
    #     dr.find_element_by_id('su').click()
    # @unittest.skip('就是不想执行测试，任性')
    def test_2(self):
        print(2)
    # @unittest.skipIf(1<2,'这是if的理由')
    def test_3(self):
        print(3)
    # @unittest.skipUnless(1>2,'这是Unless的理由')
    def test_4(self):
        print(4)
    # @unittest.expectedFailure
    def test_5(self):
        print(5)

if __name__ == '__main__':
    unittest.main()