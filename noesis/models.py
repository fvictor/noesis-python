import javabridge as jb
from .network import *
from .utils import get_class_wrapper

class NetworkModel(Network):
    """A network generated using a network formation model.
    
    """

    def __init__(self, model, *args):
        class_wrapper = get_class_wrapper(model, ['noesis.model.random', 'noesis.model.regular'], 'Network')
        network = class_wrapper(*args)
        super(NetworkModel, self).__init__(from_network=network)