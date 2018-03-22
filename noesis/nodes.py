import javabridge as jb
from .utils import get_class_wrapper, java_collection_to_numpy

class NodeScorer():
    """A scorer for network nodes.
    
    """

    def __init__(self, scorer, *args):
        self.scorer = scorer
        self.args = args

    def compute(self, network):
        class_wrapper = get_class_wrapper(self.scorer, ['noesis.analysis.structure'])
        scorer = class_wrapper(network.__o__, *self.args)
        return java_collection_to_numpy(scorer.call(), float)