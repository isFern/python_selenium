import unittest
# import HTMLTestRunner
from HTMLTestRunner_Py3 import HTMLTestRunner
import time
import os
from test_case.linghang_fina import LinghangTest

current_path = os.getcwd()
# cash_path = os.path.join(current_path, "TestCase")
report_path = os.path.join(current_path, "")
# print(report_path)

if __name__ == '__main__':
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # 报告地址&名称
    report_title = '领航报告' + now + '.html'
    result_path = os.path.join(report_path, report_title)
    # 报告描述
    desc = '用于展示修改样式后的HTMLTestRunner'
    testsuite = unittest.TestSuite()
    # 一个一个添加测试用例，且按照添加的顺序执行
    testsuite.addTest(LinghangTest('test_1Login'))
    testsuite.addTest(LinghangTest('test_Customer'))

    with open(result_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
        '''
        result = runner.run(testsuite)
        num1 = result.testsRun				# 运行测试用例的总数
        num2 = result.success_count			# 运行测试用例成功的个数
        num3 = result.failure_count			# 运行测试用例失败的个数
        print(num1, num2, num3)
        '''
