import javabridge as jb
from .utils import get_class_wrapper, java_int_array_to_list

class Network:
    """A network.
    
    """
    def __init__(self, **kargs):
        if 'from_network' in kargs:
            self.__o__ = kargs['from_network']
        else:
            class_wrapper = get_class_wrapper('AttributeNetwork', ['noesis'])
            self.__o__ = class_wrapper()

    def is_directed(self):
        return self.__o__.isDirected()

    def set_directed(self, directed):
        return self.__o__.setDirected(directed)

    def nodes(self):
        return self.__o__.nodes()
    
    def links(self):
        return self.__o__.links()

    def in_links(self, node):
        return java_int_array_to_list(self.__o__.inLinks(node))

    def out_links(self, node):
        return java_int_array_to_list(self.__o__.outLinks(node))

    def degree(self, node):
        return self.__o__.degree(node)

    def in_degree(self, node):
        return self.__o__.inDegree(node)

    def out_degree(self, node):
        return self.__o__.outDegree(node)

    def add_node(self, node):
        self.__o__.add(node)

    def remove_node(self, node):
        self.__o__.remove(node)

    def contains_node(self, node):
        return self.__o__.contains(node)

    def add_link(self, source, target):
        self.__o__.add(source, target)

    def add_link2(self, source, target):
        self.__o__.add2(source, target)

    def remove_link(self, source, target):
        self.__o__.remove(source, target)

    def remove_link2(self, source, target):
        self.__o__.remove2(source, target)

    def contains_link(self, source, target):
        return self.__o__.contains(source, target)