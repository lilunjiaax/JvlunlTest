import unittest
from unit_test.git_attr import Dict

from .unit_test_frame import TestDict  # 把测试驱动的类导入

if __name__ == "__main__":
    suite = unittest.TestSuite()

    tests = [TestDict('test_init'), TestDict('test_key'),
             TestDict('test_attr'), TestDict('test_keyerror')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)








