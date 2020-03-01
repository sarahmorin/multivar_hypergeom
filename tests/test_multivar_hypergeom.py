#!/usr/bin/env python3

"""Tests for `multivar_hypergeom` package."""

import pytest

from multivar_hypergeom.multivar_hypergeom import MultivarHypergeom


class TestCreationMethod:
    def test_list(self):
        test = MultivarHypergeom([10, 10, 10])
        assert isinstance(test, MultivarHypergeom)

    def test_dict(self):
        test = MultivarHypergeom({"A": 10, "B": 10, "C": 10})
        assert isinstance(test, MultivarHypergeom)

    def test_total(self):
        test1 = MultivarHypergeom([10, 10, 10], total=30)
        test2 = MultivarHypergeom({"A": 20, "B": 10, "C": 15}, total=45)
        assert test1.init_total == 30
        assert test1.curr_total == 30
        assert test2.init_total == 45
        assert test2.curr_total == 45

    def test_type_num(self):
        assert MultivarHypergeom([0, 0, 0]).num_types == 3
        assert MultivarHypergeom({"a": 0, "b": 0}).num_types == 2

    def test_exceptions(self):
        with pytest.raises(Exception):
            MultivarHypergeom([0], names=[" ", " "])
        with pytest.raises(Exception):
            MultivarHypergeom([0, 1, 2], names=[" ", " "])
        with pytest.raises(Exception):
            MultivarHypergeom({"A": 0}, names=[" "])
        with pytest.raises(TypeError):
            MultivarHypergeom([0.5])
        with pytest.raises(TypeError):
            MultivarHypergeom({"A": 0.5})
        with pytest.raises(TypeError):
            MultivarHypergeom([" "])
        with pytest.raises(TypeError):
            MultivarHypergeom({"A": "10"})
        with pytest.raises(ValueError):
            MultivarHypergeom([1, 2], total=1)
        with pytest.raises(ValueError):
            MultivarHypergeom([10, 20], total=100)


class TestSamplingMethod:
    def test_exceptions(self):
        test = MultivarHypergeom([1, 2, 3])
        with pytest.raises(TypeError):
            test.sample(2.5)
        with pytest.raises(TypeError):
            test.sample("nine")
        with pytest.raises(ValueError):
            test.sample(0)
        with pytest.raises(ValueError):
            test.sample(-2)
        with pytest.raises(ValueError):
            test.sample(500)
        test.sample(6)
        with pytest.raises(Exception):
            test.sample(2)

    def simple_list(self):
        test1 = MultivarHypergeom([10, 20, 30])
        sample1 = test1.sample(30)
        assert sum(sample1) == 30
        assert sample1[0] >= 0 and sample1[0] <= 10
        assert sample1[1] >= 0 and sample1[1] <= 20
        assert sample1[2] >= 0 and sample1[2] <= 30

    def simple_dict(self):
        test1 = MultivarHypergeom({"A": 10, "B": 20, "C": 30})
        sample1 = test1.sample(30)
        assert sum(sample1) == 30
        assert sample1[0] >= 0 and sample1[0] <= 10
        assert sample1[1] >= 0 and sample1[1] <= 20
        assert sample1[2] >= 0 and sample1[2] <= 30

    def test_sample1(self):
        test1 = MultivarHypergeom({"A": 10, "B": 10})
        test2 = MultivarHypergeom([10, 10], names=["A", "B"])
        test3 = MultivarHypergeom([10, 10])
        for i in range(20):
            sample1 = test1.sample1()
            sample2 = test2.sample1()
            sample3 = test3.sample1()
            assert sample1 == "A" or sample1 == "B"
            assert sample2 == "A" or sample2 == "B"
            assert int(sample3) == 1 or int(sample3) == 0


class TestResetMethod:
    # TODO: test exceptions from poor initialization
    def test(self):
        test1 = MultivarHypergeom([10, 20, 30])
        test1.sample(20)
        assert test1.curr_total != 60
        test1.reset()
        assert test1.curr_total == 60
        assert test1.curr_counts[0] == 10
        assert test1.curr_counts[1] == 20
        assert test1.curr_counts[2] == 30


class TestStrMethods:
    def test_repr(self):
        test1 = MultivarHypergeom([10, 20, 30])
        test2 = MultivarHypergeom([10, 20, 30], names=["First", "Second", "Third"])
        test3 = MultivarHypergeom({"One": 1, "Two": 2, "Three": 3})
        assert test1.__repr__() == "MultivarHypergeom(['0', '1', '2'],[10, 20, 30],60)"
        assert (
            test2.__repr__()
            == "MultivarHypergeom(['First', 'Second', 'Third'],[10, 20, 30],60)"
        )
        assert (
            test3.__repr__() == "MultivarHypergeom(['One', 'Two', 'Three'],[1, 2, 3],6)"
        )

    def test_str(self):
        test1 = MultivarHypergeom([10, 20, 30])
        test2 = MultivarHypergeom([10, 20, 30], names=["First", "Second", "Third"])
        test3 = MultivarHypergeom({"One": 1, "Two": 2, "Three": 3})
        assert (
            test1.__str__()
            == "Types: ['0', '1', '2'] \nCounts: [10, 20, 30] \nTotal: 60"
        )
        assert (
            test2.__str__()
            == "Types: ['First', 'Second', 'Third'] \nCounts: [10, 20, 30] \nTotal: 60"
        )
        assert (
            test3.__str__()
            == "Types: ['One', 'Two', 'Three'] \nCounts: [1, 2, 3] \nTotal: 6"
        )


class TestCDFMethod:
    def test_simple(self):
        test1 = MultivarHypergeom([10, 20, 30])
        test2 = MultivarHypergeom({"A": 40, "B": 100, "C": 60})
        cdf1 = list(test1.cdf())
        cdf2 = list(test2.cdf())
        assert cdf1 == [float(1 / 6), float(3 / 6), float(6 / 6)]
        assert cdf2 == [float(4 / 20), float(14 / 20), float(20 / 20)]

    def test_large(self):
        # TODO: tests for large distributions
        return None

    def test_full(self):
        # TODO: full set of test cases
        # - Tests each round of sampling
        # - Tests for empty distributions
        # - Tests last element is always 1.0
        return None
