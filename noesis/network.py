import javabridge as jb
from .utils import get_class_wrapper, java_int_array_to_list

class Network:
    """Network.

    This class implements the interface for networks, providing methods to query and manipulate
    network nodes and links.
    
    """

    def __init__(self, **kargs):
        if 'from_network' in kargs:
            self.__o__ = kargs['from_network']
        else:
            class_wrapper = get_class_wrapper('AttributeNetwork', ['noesis'])
            self.__o__ = class_wrapper()

    def is_directed(self):
        """Check if a network is directed.

        Returns
        -------
        is_directed :  bool
            True if the network is directed, False otherwise.
        """
        return self.__o__.isDirected()

    def set_directed(self, directed):
        """Set network if network is directed or undirected.

        Parameters
        ----------
        directed : boolean
            True to set the network as directed, False otherwise.
        """
        self.__o__.setDirected(directed)

    def nodes(self):
        """Get the number of nodes in the network.

        Returns
        -------
        node_count :  integer
            Number of nodes in the network.
        """
        return self.__o__.nodes()
    
    def links(self):
        """Get the number of links in the network.

        Returns
        -------
        link_count :  integer
            Number of links in the network.
        """
        return self.__o__.links()

    def in_links(self, node):
        """Get in-links for a given node in the network.

        Parameters
        ----------
        node : integer
            Index of the node from which to obtain in-links.

        Returns
        -------
        links :  list of integers
            List of indices of nodes with links to the specified node.
        """
        return java_int_array_to_list(self.__o__.inLinks(node))

    def out_links(self, node):
        """Get out-links for a given node in the network.

        Parameters
        ----------
        node : integer
            Index of the node from which to obtain out-links.

        Returns
        -------
        links :  list of integers
            List of indices of nodes with links from the specified node.
        """
        return java_int_array_to_list(self.__o__.outLinks(node))

    def degree(self, node):
        """Get the degree of a given node in the network.

        Parameters
        ----------
        node : integer
            Index of the node from which to obtain the degree.

        Returns
        -------
        degree :  integer
            Degree of the node.
        """
        return self.__o__.degree(node)

    def in_degree(self, node):
        """Get the in-degree of a given node in the network.

        Parameters
        ----------
        node : integer
            Index of the node from which to obtain the in-degree.

        Returns
        -------
        degree :  integer
            In-degree of the node.
        """
        return self.__o__.inDegree(node)

    def out_degree(self, node):
        """Get the out-degree of a given node in the network.

        Parameters
        ----------
        node : integer
            Index of the node from which to obtain the out-degree.

        Returns
        -------
        degree :  integer
            Out-degree of the node.
        """
        return self.__o__.outDegree(node)

    def add_node(self):
        """Add a node to the network.

        Returns
        -------
        index :  integer
            Index of the added node.
        """
        index = self.nodes()
        self.__o__.add(index)

    def remove_node(self, node):
        """Remove a given node from the network.

        Parameters
        ----------
        node : integer
            Index of the node to remove.
        """
        self.__o__.remove(node)

    def contains_node(self, node):
        """Check if the network contains a node.

        Parameters
        ----------
        node : integer
            Index of the node to check.

        Returns
        -------
        is_contained :  boolean
            True if the network contains the node, False otherwise.
        """
        return self.__o__.contains(node)

    def add_link(self, source, target):
        """Add a directed link to the network.

        Parameters
        ----------
        source : integer
            Index of the source node.
        target : integer
            Index of the target node.
        """
        self.__o__.add(source, target)

    def add_link2(self, source, target):
        """Add an undirected link to the network.

        Parameters
        ----------
        source : integer
            Index of the source node.
        target : integer
            Index of the target node.
        """
        self.__o__.add2(source, target)

    def remove_link(self, source, target):
        """Remove a directed link from the network.

        Parameters
        ----------
        source : integer
            Index of the source node.
        target : integer
            Index of the target node.
        """
        self.__o__.remove(source, target)

    def remove_link2(self, source, target):
        """Remove an undirected link from the network.

        Parameters
        ----------
        source : integer
            Index of the source node.
        target : integer
            Index of the target node.
        """
        self.__o__.remove2(source, target)

    def contains_link(self, source, target):
        """Check if the network contains a link.

        Parameters
        ----------
        source : integer
            Index of the source node.
        target : integer
            Index of the target node.

        Returns
        -------
        is_contained :  boolean
            True if the network contains the link, False otherwise.
        """
        return self.__o__.contains(source, target)