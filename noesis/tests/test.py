import unittest
from noesis import Noesis

class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.ns = Noesis()
        network_reader = self.ns.create_network_reader('GML')
        self.network = network_reader.read('noesis/data/karate.gml')

    # Network
    def test_read_network(self):
        self.assertEqual(self.network.is_directed(), False)
        self.assertEqual(self.network.nodes(), 34)
        self.assertEqual(self.network.links(), 156)
        self.assertEqual(self.network.degree(0), 16)
        self.assertEqual(self.network.in_degree(0), 16)
        self.assertEqual(self.network.out_degree(0), 16)
        self.assertEqual(len(self.network.in_links(0)), 16)
        self.assertEqual(len(self.network.out_links(0)), 16)
        self.assertEqual(self.network.contains_link(5,6), True)

    def test_network(self):
        net = self.ns.create_network()
        self.assertEqual(net.nodes(), 0)
        self.assertEqual(net.links(), 0)

        source = net.add_node()
        target = net.add_node()
        net.add_link(source, target)
        self.assertEqual(net.nodes(), 2)
        self.assertEqual(net.links(), 1)
        self.assertEqual(net.contains_link(source, target), True)

        new = net.add_node()
        self.assertEqual(len(net.out_links(new)), 0)

    # Models
    def test_erdos_renyi_model(self):
        erdos_renyi_network = self.ns.create_network_from_model('ErdosRenyi', 100, 300)
        self.assertEqual(erdos_renyi_network.nodes(), 100)
        self.assertEqual(erdos_renyi_network.links(), 300)

    # Community detection
    def test_community_detection(self):
        community_detector = self.ns.create_community_detector('KernighanLin')
        communities = community_detector.compute(self.network)
        self.assertEqual(len(communities), 34)

    # Structure
    def test_closeness(self):
        closeness = self.ns.create_node_scorer('Closeness')
        result = closeness.compute(self.network)
        self.assertEqual(result.shape, (34,))

    def test_katz_centrality(self):
        katz_centrality = self.ns.create_node_scorer('KatzCentrality')
        result = katz_centrality.compute(self.network)
        self.assertEqual(result.shape, (34,))

    # Link prediction and scoring   
    def test_cn_score(self):
        cn_score = self.ns.create_link_scorer('CommonNeighbors')
        result = cn_score.compute(self.network)
        self.assertEqual(len(result), 156)

    def test_cn_prediction(self):
        pa_scorer = self.ns.create_link_predictor('CommonNeighbors')
        result = pa_scorer.compute(self.network)
        self.assertEqual(result.shape, (34, 34))

    # Layout
    def test_layout_fruchterman_reingold(self):
        layout = self.ns.create_layout('FruchtermanReingold')
        x, y = layout.compute(self.network)
        self.assertEqual(x.shape, (34,))
        self.assertEqual(y.shape, (34,))

    def test_layout_hierarchical(self):
        layout = self.ns.create_layout('Hierarchical')
        x, y = layout.compute(self.network)
        self.assertEqual(x.shape, (34,))
        self.assertEqual(y.shape, (34,))

    def test_layout_circular(self):
        layout = self.ns.create_layout('Circular')
        x, y = layout.compute(self.network)
        self.assertEqual(x.shape, (34,))
        self.assertEqual(y.shape, (34,))

    @classmethod
    def tearDownClass(self):
        self.ns.end()

if __name__ == '__main__':
    unittest.main()