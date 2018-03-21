import javabridge as jb
from .network import *
from .utils import get_class_wrapper

class NetworkReader():

    def __init__(self, reader, *args):
        self.reader = reader
        self.args = args

    def read(self, filepath):
        class_wrapper = get_class_wrapper(self.reader, ['noesis.io'], 'NetworkReader')
        file_reader_wrapper = get_class_wrapper('FileReader', ['java.io'])
        file_reader = file_reader_wrapper(filepath)
        network_reader = class_wrapper(file_reader, *self.args)
        network = network_reader.read()
        network_reader.close()
        return Network(from_network=network)


class NetworkWriter():
    pass