import javabridge as jb
from .utils import get_class_wrapper, java_matrix_to_numpy

class LinkTask():
    """Base abstract class for link-related scores."""

    __PACKAGES__ = ['noesis.analysis.structure.links.prediction.local',
                    'noesis.analysis.structure.links.prediction.global']

    __SCORE_TAIL__ = 'Score'

class LinkScorer(LinkTask):
    """This class implements the interface for link scorers. These algorithms
    compute a score for each link according to certain specific rules.

    Parameters
    ----------
    scorer : string
        Technique used to compute link scores. Currently supported techniques are:
        - Local: 'CommonNeighbors', 'AdamicAdar', 'ResourceAllocation', 'PreferentialAttachment', 'HubDepressed', 'HubPromoted', 'Jaccard', 'LocalLeichtHolmeNewman', 'Salton', and 'Sorensen'.
        - Global: 'Katz', 'RandomWalk', 'RandomWalkWithRestart', 'FlowPropagation', 'PseudoinverseLaplacian', 'AverageCommuteTime', 'RandomForestKernel', and 'GlobalLeichtHolmeNewman'.

    args: parameters
        Parameters for the link scorer. These parameters are specific
        for each link scorer and more details are provided in NOESIS documentation.
    
    """

    def __init__(self, scorer, *args):
        self.scorer = scorer
        self.args = args

    def compute(self, network):
        """Compute scores for each link in a given network.

        Parameters
        ----------
        network : Network
            Network for which the link scores will be computed.

        Returns
        -------
        scores :  list of tuples
            A list of tuples with the format (source_node, target_node, link_score).
        """
        class_wrapper = get_class_wrapper(self.scorer, LinkScorer.__PACKAGES__, LinkScorer.__SCORE_TAIL__)
        link_predictor = class_wrapper(network.__o__, *self.args)
        scorer_wrapper = get_class_wrapper('LinkScorer', ['noesis.analysis.structure.links.scoring'])
        link_scorer = scorer_wrapper(network.__o__, link_predictor)
        scores = link_scorer.call()
        link_index = link_scorer.getLinkIndex()
        result = [(link_index.source(i), link_index.destination(i), scores.get(i)) for i in range(link_index.links())]
        return result

class LinkPredictor(LinkTask):
    """This class implements the interface for link predictors. These algorithms
    compute a score for each pair of nodes according to certain specific rules.

    Parameters
    ----------
    scorer : string
        Technique used to compute node pair scores. Currently supported techniques are:
        - Local: 'CommonNeighbors', 'AdamicAdar', 'ResourceAllocation', 'PreferentialAttachment', 'HubDepressed', 'HubPromoted', 'Jaccard', 'LocalLeichtHolmeNewman', 'Salton', and 'Sorensen'.
        - Global: 'Katz', 'RandomWalk', 'RandomWalkWithRestart', 'FlowPropagation', 'PseudoinverseLaplacian', 'AverageCommuteTime', 'RandomForestKernel', and 'GlobalLeichtHolmeNewman'.

    args: parameters
        Parameters for the link predictor. These parameters are specific
        for each link predictor and more details are provided in NOESIS documentation.
    
    """

    def __init__(self, predictor, *args):
        self.predictor = predictor
        self.args = args

    def compute(self, network):
        """Compute scores for each pair of nodes in a given network.

        Parameters
        ----------
        network : Network
            Network for which the node pair scores will be computed.

        Returns
        -------
        scores :  ndarray, shape (num_nodes,num_nodes)
            Matrix of node pair scores.
        """
        class_wrapper = get_class_wrapper(self.predictor, LinkPredictor.__PACKAGES__, LinkScorer.__SCORE_TAIL__)
        link_predictor = class_wrapper(network.__o__, *self.args)
        matrix = link_predictor.call()
        return java_matrix_to_numpy(matrix)