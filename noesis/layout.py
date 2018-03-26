import javabridge as jb
from .utils import get_class_wrapper, java_collection_to_numpy

class Layout():
    """This class implements the interface for network layouts. These algorithms
    compute visual coordinates for each node to obtain a more pleasant
    visualization of the network.

    Parameters
    ----------
    layout : string
        Technique used to compute the layout. Currently supported techniques are
        'Random', 'KamadaKawai', 'FruchtermanReingold', 'Hierarchical', 'Linear', 'Mesh',
        'Radial',  BinaryTree', 'Circular', 'Hypercube', 'Star', and 'Toroidal'.

    args: parameters
        Parameters for the layout algorithm. These parameters are specific
        for each algorithm and more details are provided in NOESIS documentation.
    
    """

    def __init__(self, layout, *args):
        self.layout = layout
        self.args = args

    def compute(self, network):
        """Compute a layout for a given network.

        Parameters
        ----------
        network : Network
            Network for which the layout will be computed.

        Returns
        -------
        x :  ndarray, shape (num_nodes,)
            Vector of x coordinates for each node.
        y :  ndarray, shape (num_nodes,)
            Vector of y coordinates for each node.
        """
        class_wrapper = get_class_wrapper(self.layout, ['noesis.algorithms.visualization'], 'Layout')
        layout = class_wrapper(*self.args)
        att_wrapper = get_class_wrapper('Attribute', ['noesis'])
        x = att_wrapper('x')
        y = att_wrapper('y')
        layout.layout(network.__o__, x, y)
        transform = lambda v: float(v.doubleValue())
        x = java_collection_to_numpy(x, transform)
        y = java_collection_to_numpy(y, transform)
        return x, y