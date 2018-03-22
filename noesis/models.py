import javabridge as jb
from .network import Network
from .utils import get_class_wrapper

class NetworkModel(Network):
    """Network model.

    This class implements the interface for network models, allowing to instantiate a network given
    a network formation model.

    Parameters
    ----------
    model : string
        Network formation model used to generate the network. Currently supported models are
        'ErdosRenyi', 'BarabasiAlbert', 'WattsStrogatz', 'Gilbert', 'PriceCitation', 'AnchoredRandom',
        'ConnectedRandom', 'Complete', 'BinaryTree', 'Hypercube', 'Isolate', 'Mesh', 'Ring', 'Star',
        'Tandem', and 'Toroidal'.

    args: parameters
        Parameters the for network formation model. These parameters are specific
        for each network formation model and more details are provided in NOESIS documentation.
    
    """

    def __init__(self, model, *args):
        class_wrapper = get_class_wrapper(model, ['noesis.model.random', 'noesis.model.regular'], 'Network')
        network = class_wrapper(*args)
        super(NetworkModel, self).__init__(from_network=network)