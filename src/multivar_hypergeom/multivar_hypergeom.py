"""
    Module for sampling from multivariate hypergeometric distribution.
"""

__all__ = ["MultivarHypergeom"]
__version__ = "0.0.1"
__author__ = "Sarah Morin"

from typing import List

import numpy as np


class MultivarHypergeom(object):
    """
    Class for multivariate hypergeometric distribution objects.

    Attributes:
        init_total: Initial total size of the distribution.
        curr_total: Current total size of the distribtuion.
        init_counts: Initial counts of each item type.
        curr_counts: Current counts of each item type after 0 or more sample.
        type_names: Name/ID for each item type.
        num_types: Number of different item types.
    """

    init_total: int = 0
    curr_total: int = 0
    init_counts: List[int] = None
    curr_counts: List[int] = None
    type_names: List[str] = None
    num_types: int = 0

    def __init__(self, counts, names: List[str] = None, total: int = None):

        """
        Creating a distribution object.

        Args:
            counts: Counts of item types in distribution. Can be list of integers or
                dict of string keys with integer values. Length of list gives num_types.
                If no total is passed in, both init_total and curr_total are initialized
                to sum of type counts passed in.
            names: List of strings which identify different types of items in
                distribution. Length must be equal to num_types. Cannot be used in
                addition to dict type counts.
            total: Integer total size of distribution. If counts contained integer
                values, should be equal to sum of those counts.
        """
        if type(counts) is list and all(isinstance(n, int) for n in counts):
            self.init_counts = list(counts)
            self.curr_counts = list(counts)

            if names:
                if len(names) != len(counts):
                    raise Exception(
                        "Incompatible lengths: type names and counts must be equal length"
                    )

                self.type_names = names
            else:
                self.type_names = list()
                for i in range(len(counts)):
                    self.type_names.append(str(i))

        elif (
            type(counts) is dict
            and all(isinstance(k, str) for k in counts.keys())
            and all(isinstance(v, int) for v in counts.values())
        ):
            self.init_counts = list(counts.values())
            self.curr_counts = list(counts.values())
            self.type_names = list(counts.keys())
            if names:
                raise Exception(
                    "Too may arguments: type names input in counts and names"
                )

        else:
            raise TypeError(
                "Unsupported type: counts must be List[int] or Dict[str, int]"
            )

        if total:
            if sum(self.init_counts) != total:
                raise ValueError("Total must be equal to the sum of all object counts")
            self.init_total = total
            self.curr_total = total
        else:
            self.init_total = sum(self.init_counts)
            self.curr_total = sum(self.curr_counts)

        self.num_types = len(self.init_counts)

    def __repr__(self):
        return "MultivarHypergeom({},{},{})".format(
            self.type_names, self.curr_counts, self.curr_total
        )

    def __str__(self):
        return "Types: {} \nCounts: {} \nTotal: {}".format(
            self.type_names, self.curr_counts, self.curr_total
        )

    def cdf(self) -> np.ndarray:
        """
        Computes cumuliative distribution function.

        Returns:
            NumPy array of floats where each entry is the sum of proportions of items
            up to that point.
        """
        props = np.array(
            [
                self.curr_counts[i] / self.curr_total
                for i in range(len(self.curr_counts))
            ],
            dtype=float,
        )
        return np.array([sum(props[: i + 1]) for i in range(self.num_types)])

    def sample(self, size: int) -> np.ndarray:
        """
        Acquire sample of given size from current distribution.

        Args:
            size: Integer sample size desired. Must be greater than 0 and less than or
                equal to current size of distribution.

        Returns:
            NumPy array of integers where each entry represents number of items of that
            type found in sample. These items have been removed from the distribution.
        """
        if type(size) is not int:
            raise TypeError("size must be integer value")
        if size <= 0 or size > self.curr_total:
            raise ValueError("Invalid size")
        if self.curr_total == 0:
            raise Exception("Empty sample space")
        sample_counts = np.zeros(self.num_types, dtype=int)
        sample_size = 0

        while sample_size < size:
            rv = np.random.random()
            cdf = self.cdf()

            for i in range(self.num_types):
                if rv < cdf[i] and self.curr_counts[i] > 0:
                    sample_counts[i] += 1
                    self.curr_counts[i] -= 1
                    sample_size += 1
                    self.curr_total -= 1
                    break

        return sample_counts

    def sample1(self) -> str:
        """
        Sample 1 item from current distribution.

        Returns:
            Item type (as string) of 1 sampled item.
        """
        if self.curr_total == 0:
            raise Exception("Empty sample space")
        cdf = self.cdf()
        rv = np.random.random()
        for i in range(self.num_types):
            if rv < cdf[i] and self.curr_counts[i] > 0:
                self.curr_counts[i] -= 1
                self.curr_total -= 1
                return self.type_names[i]
        return None

    def reset(self) -> None:
        """Resets distribution to initial state."""
        if self.init_total == 0 or self.init_counts is None:
            raise Exception("Instantiation Error: initial values not stored correctly")

        self.curr_total = self.init_total
        for i in range(self.num_types):
            self.curr_counts[i] = self.init_counts[i]
        return None
