import unittest
class Testcase(unittest.TestCase):
        def setUp(self):
                print('setup method execution')
        def test(self):
                print('test method execution')
				print(10/0)#for testing of unit testfailre scenario
        def tearDown(self):
                print('teardown method execution')
unittest.main()
