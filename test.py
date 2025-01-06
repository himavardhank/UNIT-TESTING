import unittest
class Testcase(unittest.TestCase):
        def setUp(self):
                print('setup method execution')
        def test_method1(self):
                print('test method1 execution')
        def test_method2(self):
                print('test method2 execution')
        def tearDown(self):
                print('teardown')
unittest.main()

#for using different test methods

