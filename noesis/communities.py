import javabridge as jb
import numpy as np
from .utils import get_class_wrapper, java_one_row_matrix_to_list

class CommunityDetector():

    __PACKAGES__ = ['noesis.algorithms.communities.hierarchical.agglomerative',
                    'noesis.algorithms.communities.hierarchical.divisive',
                    'noesis.algorithms.communities.modularity',
                    'noesis.algorithms.communities.overlapping',
                    'noesis.algorithms.communities.partitioning',
                    'noesis.algorithms.communities.spectral']

    def __init__(self, detector, *args):
        self.detector = detector
        self.args = args

    def compute(self, network):
        class_wrapper = get_class_wrapper(self.detector, CommunityDetector.__PACKAGES__)
        detector = class_wrapper(network.__o__, *self.args)
        detector.compute()
        result = detector.getResults()
        return java_one_row_matrix_to_list(result, int)