from unittest import TestCase
from pkg_resources import resource_filename
from noesis import Noesis

class Tests(TestCase):

    @classmethod
    def setUpClass(self):
        self.ns = Noesis()
        network_reader = self.ns.create_network_reader('GML')
        self.network = network_reader.read('noesis/data/karate.gml')

    # Network
    def test_network(self):
        self.assertEqual(self.network.is_directed(), False)
        self.assertEqual(self.network.nodes(), 34)
        self.assertEqual(self.network.links(), 156)
        self.assertEqual(self.network.degree(0), 16)
        self.assertEqual(self.network.in_degree(0), 16)
        self.assertEqual(self.network.out_degree(0), 16)
        self.assertEqual(len(self.network.in_links(0)), 16)
        self.assertEqual(len(self.network.out_links(0)), 16)
        self.assertEqual(self.network.contains_link(5,6), True)

    # Models
    def test_erdos_renyi_model(self):
        erdos_renyi_network = self.ns.create_network_from_model('ErdosRenyi', 100,300)
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
        self.assertEqual(len(result), 34)

    def test_katz_centrality(self):
        katz_centrality = self.ns.create_node_scorer('KatzCentrality')
        result = katz_centrality.compute(self.network)
        self.assertEqual(len(result), 34)

    # Link prediction and scoring   
    def test_cn_score(self):
        cn_score = self.ns.create_link_scorer('CommonNeighbors')
        result = cn_score.compute(self.network)
        self.assertEqual(len(result), 156)

    def test_cn_prediction(self):
        pa_scorer = self.ns.create_link_predictor('CommonNeighbors')
        result = pa_scorer.compute(self.network)
        self.assertEqual(len(result), 34)
        self.assertEqual(len(result[0]), 34)

    # Layout
    def test_layout(self):
        layout = self.ns.create_layout('Circular')
        x, y = layout.compute(self.network)
        self.assertEqual(len(x), 34)
        self.assertEqual(len(y), 34)

    @classmethod
    def tearDownClass(self):
        self.ns.end()

if __name__ == '__main__':
    unittest.main()