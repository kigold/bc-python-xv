import unittest
from two_sum import two_sum
class TwoSumTestSuite(unittest.TestCase):
	def test_unit_range_4(self):
		res = two_sum([2,5,1,7],8)
		self.assertEqual(res, [2, 3])

	def test_unit_range_5(self):
		res = two_sum([3,5,1,7,4],9)
		self.assertEqual(res, [1,4])

	def test_unit_range_6(self):
		res = two_sum([2,1,5,3,7,9],4)
		self.assertEqual(res, [1,3])

	def test_list_range_7(self):
		res = two_sum([2,5,1,7,4,2,9],8)
		self.assertEqual(res, [2, 3])

	def test_list_range_8(self):
		result = two_sum([7,9,10,8,6, 1,3,5],18)
		self.assertEqual(result, [2,3])

	def test_list_range_9(self):
		result = two_sum([2,9,15,8,6,7,1,3,14],13)
		self.assertEqual(result, [4,5])

	def test_list_range_10(self):
		result = two_sum([1,10,14,8,6,5,4,3,54,20], 12)
		self.assertEqual(result, [3, 6])

if __name__ =="__main__":
	unittest.main()

    
