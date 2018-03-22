import javabridge as jb
import numpy as np
from .utils import get_class_wrapper, java_one_row_matrix_to_list

class CommunityDetector():
    """Community detector.

    This class implements the interface for community detectors. These algorithms
    find groups of densely connected nodes.

    Parameters
    ----------
    detector : string
        Technique used for community detection. Currently supported techniques are:
        - Hierarchical agglomerative: 'SingleLink', 'AverageLink', and 'CompleteLink'.
        - Hierarchical divisive: 'NewmanGirvan' and 'Radicchi'.
        - Modularity-based: 'FastGreedy' and 'MultiStepGreedy'.
        - Partitioning-based: 'KernighanLin' and 'KMeans'.
        - Spectral: 'UKMeans', 'NJW', and 'EIG1'.
        - Overlapping: 'BigClam'.

    args: parameters
        Parameters for the community detector. These parameters are specific
        for each algorithm and more details are provided in NOESIS documentation.
    
    """

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
        """Compute node communities for a given network.

        Parameters
        ----------
        network : Network
            Network for which the communities will be computed.

        Returns
        -------
        communities :  list of integers
            A list of integers indicating the community that each node belongs to.
        """
        class_wrapper = get_class_wrapper(self.detector, CommunityDetector.__PACKAGES__, 'CommunityDetector')
        detector = class_wrapper(network.__o__, *self.args)
        detector.compute()
        result = detector.getResults()
        return java_one_row_matrix_to_list(result, int)