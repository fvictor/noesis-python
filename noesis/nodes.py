import javabridge as jb
from .utils import get_class_wrapper, java_collection_to_numpy

class NodeScorer():
    """This class implements the interface for node scorers. These algorithms
    compute a score for each node according to certain specific rules.

    Parameters
    ----------
    scorer : string
        Technique used to compute node scores. Currently supported techniques are
        'AdjustedBetweenness', 'AdjustedCloseness', 'AveragePathLength', 'Betweenness', 'BetweennessScore',
        'Closeness', 'ClusteringCoefficient', 'ConnectedComponents', 'Decay', 'Degree', 'DegreeAssortativity',
        'DiffusionCentrality', 'Eccentricity', 'EigenvectorCentrality', 'FreemanBetweenness',
        'HITS', 'InDegree', 'KatzCentrality', 'LinkBetweenness', 'LinkBetweennessScore',
        'LinkEmbeddedness', 'LinkNeighborhoodOverlap', 'LinkNeighborhoodSize', 'LinkRays',
        'NormalizedBetweenness', 'NormalizedDecay', 'NormalizedDegree', 'NormalizedInDegree',
        'NormalizedOutDegree', 'OutDegree', 'PageRank', 'PathLength', and 'UnbiasedDegreeAssortativity'.

    args: parameters
        Parameters for the node scorer. These parameters are specific
        for each node scorer and more details are provided in NOESIS documentation.
    
    """

    def __init__(self, scorer, *args):
        self.scorer = scorer
        self.args = args

    def compute(self, network):
        """Compute scores for each node in a given network.

        Parameters
        ----------
        network : Network
            Network for which the node scores will be computed.

        Returns
        -------
        scores :  ndarray, shape (num_nodes,)
            Vector of scores for each node.
        """
        class_wrapper = get_class_wrapper(self.scorer, ['noesis.analysis.structure'])
        scorer = class_wrapper(network.__o__, *self.args)
        return java_collection_to_numpy(scorer.call(), float)