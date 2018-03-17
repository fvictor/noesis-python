from pkg_resources import resource_filename
import javabridge as jb
from .network import *
from .io import *
from .communities import *
from .links import *
from .nodes import *
from .models import *
from .layout import *

class Noesis:

    DEFAULT_JAR_FILE = 'data/noesis-analyzer.lsp.201708.jar'

    def __init__(self):
        try:
            jb.start_vm(class_path=[*jb.JARS, resource_filename('noesis', Noesis.DEFAULT_JAR_FILE)], run_headless=False)
        except:
            jb.kill_vm()

    def end(self):
        jb.kill_vm()

    def launch_analyzer(self, show_splash=False):
        params = []
        if not show_splash:
            params.append('no-splash')
        class_wrapper = jb.JClassWrapper('noesis.ui.model.NetworkAnalyzerApplication')
        class_wrapper.main(params)

    def create_network_from_model(self, model, *args):
        return NetworkModel(model, *args)

    def create_network_reader(self, reader, *args):
        return NetworkReader(reader, *args)

    def create_community_detector(self, detector, *args):
        return CommunityDetector(detector, *args)

    def create_layout(self, layout, *args):
        return Layout(layout , *args)

    def create_node_scorer(self, scorer, *args):
        return NodeScorer(scorer, *args)

    def create_link_scorer(self, scorer, *args):
        return LinkScorer(scorer, *args)

    def create_link_predictor(self, predictor, *args):
        return LinkPredictor(predictor, *args)