from a import fun
import unittest
class FunTest(unittest.TestCase):
	"""
	app login
	app unser instance creation
	# before processing
	using user instamce going to call the functions. processing
	# after proicesssing
	logout
	"""
	@classmethod
	def setUpClass(cls):
		print "login"
	@classmethod
	def tearDownClass(cls):
		print "logout"
	def setUp(self):
		print "code before executing every test case"
	def tearDown(self):
		print "code after executing every test case"
	def test_12_6(self):
		print "test_12_6 executing"
		exp=2
		real=fun(12,6)
		self.assertEqual(exp,real,"test_12_6 failed")
	def test_12_0(self):
		print "test_12_0 executing"
		exp=None
		real=fun(12,0)
		self.assertEqual(exp,real,"test_12_0 failed")
	def test_str_str(self):
		print "test_str_str executing"
		exp=None
		real=fun("sdfsdf","sdfdsf")
		self.assertEqual(exp,real,"test_str_str failed")
	def ownmethod(self):
		print "own method@@@@@@@@@@@@@@"
unittest.main()