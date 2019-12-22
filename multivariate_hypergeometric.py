#
# Author: Sarah Morin
#

import math
import numpy as np
from typing import Union
from typing import List
from typing import Dict

InputDist = Union[List[int], Dict[str, int]]

class MultivarHG(object):
    init_total: int = 0
    curr_total: int = 0
    init_counts: List[int] = None
    curr_counts: List[int] = None
    type_names: List[str] = None
    type_num: int = 0


    def __init__(self, counts,
            names: List[str] = None, total: int = None):

        if type(counts) is list and all(isinstance(n, int) for n in counts):
            self.init_counts = counts
            self.curr_counts = counts

            if names:
                if len(names) != len(counts):
                    raise Exception('Incompatible lengths: type names and counts must be equal length')

                self.type_names = names

        elif type(counts) is dict and all(isinstance(k, str) for k in counts.keys()) and all(isinstance(v, int) for v in counts.values()):
            self.init_counts = counts.values()
            self.curr_counts = counts.values()
            self.type_names = counts.keys()
            if names:
                raise Exception('Too may arguments: type names input in counts and names')

        else:
            raise TypeError('Unsupported type: counts must be List[int] or Dict[str, int]')

        if total:
            self.init_total = total
            self.curr_total = total
        else:
            self.init_total = sum(self.init_counts)
            self.curr_total = sum(self.curr_counts)

        self.type_num = len(self.init_counts)

    def __repr__(self):
        return 'MultivarHG({},{},{})'.format(self.type_names, self.curr_counts, self.curr_total)

    def __str__(self):
        return 'Types: {} \n \
                Counts: {} \n \
                Total: {}'.format(self.type_names, self.curr_counts, self.curr_total)

    def cdf(self) -> np.ndarray:
        # Calculate proportions of counts to total
        props = np.array([self.curr_counts[i]/self.curr_total for i in range(len(self.curr_counts))], dtype=[float])
        return np.array([sum(props[i+1]) for i in range(len(props))])

    def sample(self, size:int) -> np.ndarray:
        # TODO
        return None

    def reset(self) -> None:
        if self.init_total is 0 or self.init_counts is None:
            raise Exception('Instantiation Error: initial values not stored correctly')

        self.curr_total = self.init_total
        self.curr_counts = self.init_counts
