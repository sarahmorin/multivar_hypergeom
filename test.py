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
        self.assertRaises(Exception, MultivarHG, {'A': 0}, names=[' '])
        self.assertRaises(TypeError, MultivarHG, [0.5])
        self.assertRaises(TypeError, MultivarHG, [' '])
        self.assertRaises(TypeError, MultivarHG, {'A': 0.5})
        self.assertRaises(TypeError, MultivarHG, {'A': 'a'})


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

    def simple(self):
        test1 = MultivarHG([10, 20, 30])
        sample1 = test1.sample(30)
        self.assertTrue(bool(sum(sample1) == 30))
        self.assertTrue(bool(sample1[0] >= 0 and sample1[0] <= 10))
        self.assertTrue(bool(sample1[1] >= 0 and sample1[1] <= 20))
        self.assertTrue(bool(sample1[2] >= 0 and sample1[2] <= 30))


class TestResetMethod(unittest.TestCase):
    # TODO
    def test(self):
        return None


class TestStrMethods(unittest.TestCase):
    # TODO
    def test(self):
        return None


class TestCDFMethod(unittest.TestCase):
    # TODO
    def test(self):
        return None


if __name__ == '__main__':
    unittest.main()
