import javabridge as jb
from .utils import get_class_wrapper, java_matrix_to_list_of_lists

class LinkTask():
    
    __PACKAGES__ = ['noesis.analysis.structure.links.prediction.local',
                    'noesis.analysis.structure.links.prediction.global']

    __SCORE_TAIL__ = 'Score'

class LinkScorer(LinkTask):

    def __init__(self, scorer, *args):
        self.scorer = scorer
        self.args = args

    def compute(self, network):
        class_wrapper = get_class_wrapper(self.scorer, LinkScorer.__PACKAGES__, LinkScorer.__SCORE_TAIL__)
        link_predictor = class_wrapper(network.__o__, *self.args)
        scorer_wrapper = get_class_wrapper('LinkScorer', ['noesis.analysis.structure.links.scoring'])
        link_scorer = scorer_wrapper(network.__o__, link_predictor)
        scores = link_scorer.call()
        link_index = link_scorer.getLinkIndex()
        result = [(link_index.source(i), link_index.destination(i), scores.get(i)) for i in range(link_index.links())]
        return result

class LinkPredictor(LinkTask):

    def __init__(self, predictor, *args):
        self.predictor = predictor
        self.args = args

    def compute(self, network):
        class_wrapper = get_class_wrapper(self.predictor, LinkPredictor.__PACKAGES__, LinkScorer.__SCORE_TAIL__)
        link_predictor = class_wrapper(network.__o__, *self.args)
        matrix = link_predictor.call()
        return java_matrix_to_list_of_lists(matrix)