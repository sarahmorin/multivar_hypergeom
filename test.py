"""
Unittest document for MultivarHG class.
"""

import unittest
from multivariate_hypergeometric import MultivarHG


class TestCreationMethod(unittest.TestCase):

    def test_list(self):
        test = MultivarHG([10, 10, 10])
        self.assertIsInstance(test, MultivarHG)

    def test_dict(self):
        test = MultivarHG({'A': 10, 'B': 10, 'C': 10})
        self.assertIsInstance(test, MultivarHG)

    def test_total(self):
        test1 = MultivarHG([10, 10, 10], total=30)
        test2 = MultivarHG({'A': 20, 'B': 10, 'C': 15}, total=45)
        self.assertEqual(test1.init_total, 30)
        self.assertEqual(test1.curr_total, 30)
        self.assertEqual(test2.init_total, 45)
        self.assertEqual(test2.curr_total, 45)

    def test_type_num(self):
        self.assertEqual(MultivarHG([0, 0, 0]).type_num, 3)
        self.assertEqual(MultivarHG({'a': 0, 'b': 0}).type_num, 2)

    def test_exceptions(self):
        self.assertRaises(Exception, MultivarHG, [0], names=[' ', ' '])
        self.assertRaises(Exception, MultivarHG, [0, 1, 2], names=[' ', ' '])
        self.assertRaises(Exception, MultivarHG, {'A': 0}, names=[' '])
        self.assertRaises(TypeError, MultivarHG, [0.5])
        self.assertRaises(TypeError, MultivarHG, [' '])
        self.assertRaises(TypeError, MultivarHG, {'A': 0.5})
        self.assertRaises(TypeError, MultivarHG, {'A': 'a'})
        self.assertRaises(ValueError, MultivarHG, [1, 2], total=1)
        self.assertRaises(ValueError, MultivarHG, [10, 20], total=100)


class TestSamplingMethod(unittest.TestCase):

    def test_exceptions(self):
        test = MultivarHG([1, 2, 3])
        self.assertRaises(TypeError, test.sample, 2.5)
        self.assertRaises(TypeError, test.sample, 'nine')
        self.assertRaises(ValueError, test.sample, 0)
        self.assertRaises(ValueError, test.sample, -2)
        self.assertRaises(ValueError, test.sample, 500)
        test.sample(6)
        self.assertRaises(Exception, test.sample, 2)

    def simple_list(self):
        test1 = MultivarHG([10, 20, 30])
        sample1 = test1.sample(30)
        self.assertTrue(bool(sum(sample1) == 30))
        self.assertTrue(bool(sample1[0] >= 0 and sample1[0] <= 10))
        self.assertTrue(bool(sample1[1] >= 0 and sample1[1] <= 20))
        self.assertTrue(bool(sample1[2] >= 0 and sample1[2] <= 30))

    def simple_dict(self):
        test1 = MultivarHG({'A': 10, 'B': 20, 'C': 30})
        sample1 = test.sample(30)
        self.assertTrue(bool(sum(sample1) == 30))
        self.assertTrue(bool(sample1[0] >= 0 and sample1[0] <= 10))
        self.assertTrue(bool(sample1[1] >= 0 and sample1[1] <= 20))
        self.assertTrue(bool(sample1[2] >= 0 and sample1[2] <= 30))

    def test_sample1(self):
        test1 = MultivarHG({'A': 10, 'B': 10})
        test2 = MultivarHG([10, 10], names=['A', 'B'])
        test3 = MultivarHG([10, 10])
        for i in range(20):
            sample1 = test1.sample1()
            sample2 = test2.sample1()
            sample3 = test3.sample1()
            self.assertTrue(bool(sample1 is 'A' or sample1 is 'B'))
            self.assertTrue(bool(sample2 is 'A' or sample2 is 'B'))
            self.assertTrue(bool(int(sample3) == 1 or int(sample3) == 0))


class TestResetMethod(unittest.TestCase):
    # TODO: test exceptions from poor initialization
    def test(self):
        test1 = MultivarHG([10, 20, 30])
        test1.sample(20)
        self.assertNotEqual(test1.curr_total, 60)
        test1.reset()
        self.assertEqual(test1.curr_total, 60)
        self.assertEqual(test1.curr_counts[0], 10)
        self.assertEqual(test1.curr_counts[1], 20)
        self.assertEqual(test1.curr_counts[2], 30)


class TestStrMethods(unittest.TestCase):

    def test_repr(self):
        test1 = MultivarHG([10, 20, 30])
        test2 = MultivarHG([10, 20, 30], names=['First', 'Second', 'Third'])
        test3 = MultivarHG({'One': 1, 'Two': 2, 'Three': 3})
        self.assertEqual(test1.__repr__(), 'MultivarHG([\'0\', \'1\', \'2\'],[10, 20, 30],60)')
        self.assertEqual(test2.__repr__(), 'MultivarHG([\'First\', \'Second\', \'Third\'],[10, 20, 30],60)')
        self.assertEqual(test3.__repr__(), 'MultivarHG([\'One\', \'Two\', \'Three\'],[1, 2, 3],6)')

    def test_str(self):
        test1 = MultivarHG([10, 20, 30])
        test2 = MultivarHG([10, 20, 30], names=['First', 'Second', 'Third'])
        test3 = MultivarHG({'One': 1, 'Two': 2, 'Three': 3})
        # TODO


class TestCDFMethod(unittest.TestCase):
    # TODO
    def test(self):
        return None


if __name__ == '__main__':
    unittest.main()
