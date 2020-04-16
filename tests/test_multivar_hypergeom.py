#!/usr/bin/env python3

"""Tests for `multivar_hypergeom` package."""

import hypothesis.strategies as st
import numpy as np
import pytest
from hypothesis import example
from hypothesis import given
from hypothesis import settings

from multivar_hypergeom.multivar_hypergeom import MultivarHypergeom


# Creation Method Tests
def test_init_exceptions():
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


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=2, max_size=10))
@settings(max_examples=1000)
@example([10, 20, 30])
def test_init_list_only(counts):
    dist = MultivarHypergeom(counts)
    assert dist.init_total == sum(counts)
    assert dist.curr_total == sum(counts)
    assert dist.init_counts == counts
    assert dist.curr_counts == counts
    assert dist.type_names == [str(i) for i in range(len(counts))]
    assert dist.num_types == len(counts)


@given(st.dictionaries(st.text(max_size=10), st.integers(min_value=0, max_value=10000), min_size=2, max_size=10,))
@settings(max_examples=1000)
@example({"A": 100, "B": 200})
def test_init_dict_only(counts):
    dist = MultivarHypergeom(counts)
    assert dist.init_total == sum(counts.values())
    assert dist.curr_total == sum(counts.values())
    assert dist.init_counts == list(counts.values())
    assert dist.curr_counts == list(counts.values())
    assert dist.type_names == list(counts.keys())
    assert dist.num_types == len(counts)


# Sample method tests
def test_sample_exceptions():
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


def simple_list():
    test1 = MultivarHypergeom([10, 20, 30])
    sample1 = test1.sample(30)
    assert sum(sample1) == 30
    assert sample1[0] >= 0 and sample1[0] <= 10
    assert sample1[1] >= 0 and sample1[1] <= 20
    assert sample1[2] >= 0 and sample1[2] <= 30


def simple_dict():
    test1 = MultivarHypergeom({"A": 10, "B": 20, "C": 30})
    sample1 = test1.sample(30)
    assert sum(sample1) == 30
    assert sample1[0] >= 0 and sample1[0] <= 10
    assert sample1[1] >= 0 and sample1[1] <= 20
    assert sample1[2] >= 0 and sample1[2] <= 30


def test_sample1():
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


# Reset method tests
# TODO: test exceptions from poor initialization
def test_reset():
    test1 = MultivarHypergeom([10, 20, 30])
    test1.sample(20)
    assert test1.curr_total != 60
    test1.reset()
    assert test1.curr_total == 60
    assert test1.curr_counts[0] == 10
    assert test1.curr_counts[1] == 20
    assert test1.curr_counts[2] == 30


# str and repr tests
def test_repr():
    test1 = MultivarHypergeom([10, 20, 30])
    test2 = MultivarHypergeom([10, 20, 30], names=["First", "Second", "Third"])
    test3 = MultivarHypergeom({"One": 1, "Two": 2, "Three": 3})
    assert test1.__repr__() == "MultivarHypergeom(['0', '1', '2'],[10, 20, 30],60)"
    assert test2.__repr__() == "MultivarHypergeom(['First', 'Second', 'Third'],[10, 20, 30],60)"
    assert test3.__repr__() == "MultivarHypergeom(['One', 'Two', 'Three'],[1, 2, 3],6)"


def test_str():
    test1 = MultivarHypergeom([10, 20, 30])
    test2 = MultivarHypergeom([10, 20, 30], names=["First", "Second", "Third"])
    test3 = MultivarHypergeom({"One": 1, "Two": 2, "Three": 3})
    assert test1.__str__() == "Types: ['0', '1', '2'] \nCounts: [10, 20, 30] \nTotal: 60"
    assert test2.__str__() == "Types: ['First', 'Second', 'Third'] \nCounts: [10, 20, 30] \nTotal: 60"
    assert test3.__str__() == "Types: ['One', 'Two', 'Three'] \nCounts: [1, 2, 3] \nTotal: 6"


# CDF method tests
@given(st.lists(st.integers(min_value=1, max_value=10000), min_size=2, max_size=10))
@settings(max_examples=100, deadline=5000)
def test_cdf_summing_to_1(xs):
    dist = MultivarHypergeom(xs)
    assert 1 - 1e-10 < list(dist.cdf())[-1] < 1 + 1e10
    for i in range(sum(xs)):
        dist.sample1()
        assert 1 - 1e-10 < list(dist.cdf())[-1] < 1 + 1e10


def test_empty():
    test = MultivarHypergeom([1, 1, 1])
    for i in range(3):
        test.sample1()
    assert np.array_equal(test.cdf(), np.ones(3, dtype=np.float64))


# TODO: Test each entry in cdf, not just end
