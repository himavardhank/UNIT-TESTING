import unittest
class Testcase(unittest.TestCase):
        def setUp(self):
                print('setup method execution')
        def test(self):
                print('test method execution')
                #print(100/0)
        def tearDown(self):
                print('teardown')
unittest.main()

#for using different testcases 
