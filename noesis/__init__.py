from pkg_resources import resource_filename
import javabridge as jb
from .network import Network
from .io import NetworkReader
from .communities import CommunityDetector
from .links import LinkScorer, LinkPredictor
from .nodes import NodeScorer
from .models import NetworkModel
from .layout import Layout

__version__ = '0.2.1'

class Noesis:
    """This class implements the entry point for the functionality provided by this package and handles the states of the Java
    Virtual Machine required to run NOESIS in Python.

    """

    __DEFAULT_JAR_FILE__ = 'data/noesis-analyzer.lsp.201708.jar'

    def __init__(self):
        try:
            jb.start_vm(class_path=jb.JARS+[resource_filename('noesis', Noesis.__DEFAULT_JAR_FILE__)], run_headless=False)
        except:
            jb.kill_vm()

    def end(self):
        """End the NOESIS session. This method must be called in order to properly end the program execution."""
        jb.kill_vm()

    def launch_analyzer(self, show_splash=False):
        """Launchs the NOESIS graphic user interface.

        Parameters
        ----------
        show_splash : bool, default False
            True to show the splash screen, False otherwise.
        """
        params = []
        if not show_splash:
            params.append('no-splash')
        class_wrapper = jb.JClassWrapper('noesis.ui.model.NetworkAnalyzerApplication')
        class_wrapper.main(params)

    def create_network(self):
        """Create a network.

        Returns
        -------
        network : Network
            A generated network.
        """
        return Network()

    def create_network_from_model(self, model, *args):
        """Create a network from a network formation model.

        Parameters
        ----------
        model : string
            Network formation model used to generate the network. See :any:`models.NetworkModel` for more details.
        args: parameters
            Parameters for the network formation model. See :any:`models.NetworkModel` for more details.

        Returns
        -------
        network : Network
            A network generated using the specified network formation model.
        """
        return NetworkModel(model, *args)

    def create_network_reader(self, reader, *args):
        """Create a network reader.

        Parameters
        ----------
        reader : string
            File format of the network reader. See :any:`io.NetworkReader` for more details.
        args: parameters
            Parameters for the network reader. See :any:`io.NetworkReader` for more details.

        Returns
        -------
        reader : NetworkReader
            A network reader with the specified parameters.
        """
        return NetworkReader(reader, *args)

    def create_community_detector(self, detector, *args):
        """Create a community detector.

        Parameters
        ----------
        detector : string
            Technique used for community detection. See :any:`communities.CommunityDetector` for more details.
        args: parameters
            Parameters for the community detector. See :any:`communities.CommunityDetector` for more details.

        Returns
        -------
        detector : CommunityDetector
            A community detector with the specified parameters.
        """
        return CommunityDetector(detector, *args)

    def create_layout(self, layout, *args):
        """Create a layout.

        Parameters
        ----------
        layout : string
            Technique used to compute the layout. See :any:`layout.Layout` for more details.
        args: parameters
            Parameters for the layout algorithm. See :any:`layout.Layout` for more details.

        Returns
        -------
        layout : Layout
            A layout with the specified parameters.
        """
        return Layout(layout , *args)

    def create_node_scorer(self, scorer, *args):
        """Create a node scorer.

        Parameters
        ----------
        scorer : string
            Technique used to compute node scores. See :any:`nodes.NodeScorer` for more details.
        args: parameters
            Parameters for the node scorer. See :any:`nodes.NodeScorer` for more details.

        Returns
        -------
        scorer : NodeScorer
            A node scorer with the specified parameters.
        """
        return NodeScorer(scorer, *args)

    def create_link_scorer(self, scorer, *args):
        """Create a link scorer.

        Parameters
        ----------
        scorer : string
            Technique used to compute link scores. See :any:`links.LinkScorer` for more details.
        args: parameters
            Parameters for the link scorer. See :any:`links.LinkScorer` for more details.

        Returns
        -------
        scorer : LinkScorer
            A link scorer with the specified parameters.
        """
        return LinkScorer(scorer, *args)

    def create_link_predictor(self, predictor, *args):
        """Create a link predictor.

        Parameters
        ----------
        scorer : string
            Technique used to compute node pair scores. See :any:`links.LinkPredictor` for more details.
        args: parameters
            Parameters for the link predictor. See :any:`links.LinkPredictor` for more details.

        Returns
        -------
        scorer : LinkPredictor
            A link predictor with the specified parameters.
        """
        return LinkPredictor(predictor, *args)