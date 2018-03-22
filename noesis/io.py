"""
Network input and output
"""

import javabridge as jb
from .network import Network
from .utils import get_class_wrapper

class NetworkReader():
    """Network reader.

    This class implements the interface for networks readers. These readers
    can load a network from a file following the specified file format.

    Parameters
    ----------
    reader : string
        File format of the network reader. Currently supported formats are
        'ASCII', 'GDF', 'GML', 'GraphML', 'Pajek', 'SNAP', and 'SNAPGZ'.

    args: parameters
        Parameters for the network reader. These parameters are specific
        for each file format and more details are provided in NOESIS documentation.
    
    """

    def __init__(self, reader, *args):
        self.reader = reader
        self.args = args

    def read(self, filepath):
        """Read a network from a specific file path.

        Parameters
        ----------
        filepath : string
            Path of the file to read.

        Returns
        -------
        network : Network
            The network that has been read from the file.
        """
        class_wrapper = get_class_wrapper(self.reader, ['noesis.io'], 'NetworkReader')
        file_reader_wrapper = get_class_wrapper('FileReader', ['java.io'])
        file_reader = file_reader_wrapper(filepath)
        network_reader = class_wrapper(file_reader, *self.args)
        network = network_reader.read()
        network_reader.close()
        return Network(from_network=network)
