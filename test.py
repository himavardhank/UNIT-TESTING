import unittest
class Testcase(unittest.TestCase):
        def setUp(self):
                print('setup method execution')
        def test(self):
                print('test method execution')
        def tearDown(self):
                print('teardown method execution')
unittest.main()
